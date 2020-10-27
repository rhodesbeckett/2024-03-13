from easy_tk import EasyTkObject
from views.MainFrame import MainFrame
from views.TestFrame import TestFrame
from views.HighlightsFrame import HighlightsFrame
from views.ChoiceFrame import ChoiceFrame
from easy_tk.helpers import grid_config_container
from models import factory_models
from controllers import *
import threading


class Root(EasyTkObject):

    def __init__(self):
        super(Root, self).__init__()
        self.create_root()
        widget = self.set_container()
        root = self.get_easy_root()
        self.set_all_frames(root, widget)
        self.geometry = "895x351"

    def set_container(self):
        self.add_just_one_from_json("views/json/scroll_bar.json", "FrameContainer")
        child = self.get("FrameContainer", False)
        master = self.easy.create_master(child.obj)
        self.easy.all_masters.setdefault("FrameContainer", master)
        return {"TkChild": child, "TkMaster": master, "name": "FrameContainer"}

    def set_all_controllers(self, models):
        self.testing = Testing(models)
        self.cutting = Cutting(models)
        self.rendering = Rendering(models)

    def get_easy_root(self):
        child = self.get("root", False)
        master = self.easy.create_master(child.get())
        return {"TkChild": child, "TkMaster": master, "name": "root"}

    def set_all_frames(self, root, widget):
        self.prozori = {}
        models = factory_models()
        self.set_all_controllers(models)

        for frame in (MainFrame, TestFrame, HighlightsFrame, ChoiceFrame):
            self.page_name = frame.__name__
            frame = frame(root, widget, self, self.set_font)
            self.prozori[self.page_name] = frame
            frame.easy.methods = [grid_config_container, ]
            frame.set_models(models)
            frame.create_widgets()

        self.easy.widgets_on_screen()
        self.switch_window("ChoiceFrame")
        self.get("root").resizable(False, False)

    def set_font(self, easy_all, widgets):
        for i in easy_all:
            for j in widgets:
                if isinstance(easy_all.get(i).get(), j):
                    easy_all.get(i).get()["font"] = ["Courier", 18]
                    break

    def render(self):
        if self.rendering.is_ready():
            self.rendering.make_txt_file()
            t_render = threading.Thread(target=self.rendering.render())
            t_render.start()
            self.testing.counter = 0
            self.cutting.cutted = False
        else:
            print("ne moze")

    def cut(self):
        if self.testing.counter == 3:
            t_cut = threading.Thread(target=lambda: self.cutting.cut_all())
            t_cut.start()
        else:
            print("ne moze")

    def refresh_testing(self):
        self.testing.counter = 0

    def test_picture(self):
        self.testing.test_photo(self.prozori[self.page_name])

    def switch_window(self, name):
        self.page_name = name
        window = self.prozori.get(name)
        window.tkraise()
        if name == "TestFrame":
            self.testing.test_all(window)