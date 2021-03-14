from easy_tk import EasyTkObject
from easy_tk import EasyTk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from views.BaseView import BaseView

class MainFrame(BaseView):

    def __init__(self,controller):
        super(MainFrame,self).__init__(controller)
        self.frame_path = "views/json/main_frame.json"

  
    def method_part(self):
        methods = {"highlights_window":self.highlights_window,
        "test_window":self.test_window,"match_button":self.match_button,
        "entry_click":self.entry_click,"cut":self.cut,"render":self.render}
        self.easy.import_methods(methods)

    def frame_part(self):
        self.set_font([Label, Button, Entry])
        self.style_all_buttons()
        self.imeage = ImageTk.PhotoImage(Image.open("bg.gif"))
        self.get("LabelBackground")["image"] = self.imeage
        self.frame_to_raise="Frame1"
        self.dimensions="950x351"

    def match_button(self, widgets):
        def open_match_src():
            frame = self.get("Frame1")
            rep = filedialog.askopenfilename(
                title="Load file",
                parent=frame,
                initialdir='/adffgdfg',
                initialfile='tmp',
                filetypes=[
                    ("All files", "*")])
            self.match.set_match(rep)

        btn_match = self.get("ButtonMatch")
        btn_match["command"] = open_match_src

    def entry_click(self, widgets):
        for i in ["EntryFirstHalfMin", "EntryFirstHalfSec", "EntrySecondHalfMin", "EntrySecondHalfSec",
                  "EntryVideosLocation"]:
            self.get(i).bind("<1>", lambda a=5: self.controller.refresh_testing())

    def render(self, widgets):
        self.get("ButtonRender")["command"] = self.controller.render

    def cut(self, widgets):
        self.get("ButtonCut")["command"] = self.controller.cut

    def highlights_window(self, widgets):
        btn_highlights = self.get("ButtonHighlights")
        btn_highlights["command"] = lambda window="HighlightsFrame": self.controller.switch_window(window)

    def test_window(self, widgets):
        btn_highlights = self.get("ButtonTestAll")
        btn_highlights["command"] = lambda window="TestFrame": self.start_test()

    def hide_entry(self):
        if self.half_time.editing_type == "first_regular":
            self.get("EntrySecondHalfMin")["state"] = "disabled"
            self.get("EntrySecondHalfSec")["state"] = "disabled"
        elif self.half_time.editing_type == "second_regular":
            self.get("EntryFirstHalfMin")["state"] = "disabled"
            self.get("EntryFirstHalfSec")["state"] = "disabled"

    def start_test(self):
        # self.half_time.set_time(.get())
        self.half_time.set_time(self.get_half_time(1))
        self.half_time.set_time(self.get_half_time(2))
        self.videos.set_src(self.get_video())
        self.controller.switch_window("TestFrame")
        self.videos.set_src(self.get_video())

    def get_half_time(self, half_time):
        if half_time == 1:
            return (self.get("EntryFirstHalfMin").get(), self.get("EntryFirstHalfSec").get())
        elif half_time == 2:
            return (self.get("EntrySecondHalfMin").get(), self.get("EntrySecondHalfSec").get())

    def get_video(self):
        return self.get("EntryVideosLocation").get()