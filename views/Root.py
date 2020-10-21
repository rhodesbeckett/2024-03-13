from tkinter import *
from views.MainFrame import MainFrame
from views.HighlightsFrame import HighlightsFrame
from views.TestFrame import TestFrame
from views.ChoiceFrame import ChoiceFrame
from models import factory_models
from controllers import *
import threading


class Root(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = self.setContainer()
        self.setAllFrames(container)
        self.prebaci_frejm("ChoiceFrame")

    def setContainer(self):
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        return container

    def setAllFrames(self, container):
        self.prozori = {}

        models = factory_models()

        for frejm in (MainFrame, HighlightsFrame, TestFrame,ChoiceFrame):
            self.page_name = frejm.__name__
            frame = frejm(container, controller=self, models=models)
            self.prozori[self.page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.set_all_controllers(models)

    def set_all_controllers(self, models):
        self.testing = Testing(models)
        self.cutting = Cutting(models)
        self.rendering = Rendering(models)

    def prebaci_frejm(self, page_name):
        self.page_name = page_name
        prozor = self.prozori[page_name]
        prozor.tkraise()

        if self.page_name == "TestFrame":
            self.geometry("1174x448")
            prozor.hide_widgets()
            self.testing.test_all(prozor.easy)

        elif self.page_name == "MainFrame":
            self.geometry("1018x436")
            if prozor.half_time.editing_type != "":
                prozor.hide_half_time()
                self.prozori["HighlightsFrame"].set_first_highlights_label()

        elif self.page_name == "HighlightsFrame":
            self.geometry("519x434")
            self.refresh_testing()

    def test_picture(self):
        self.testing.test_photo(self.prozori[self.page_name].easy)

    def cut(self):
        if self.testing.counter == 3:
            t_cut = threading.Thread(target=lambda: self.cutting.cut_all())
            t_cut.start()
        else:
            print("Not ready for cutting.")

    def render(self):
        if self.rendering.is_ready():
            self.rendering.make_txt_file()
            t_render = threading.Thread(target=self.rendering.render())
            t_render.start()
            self.testing.counter = 0
            self.cutting.cutted = False
        else:
            print("Not ready for cutting.")

    def refresh_testing(self):
        self.testing.counter = 0