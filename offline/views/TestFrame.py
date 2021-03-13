from easy_tk import EasyTkObject
from tkinter import Label,Button,Entry
from views.BaseView import BaseView

class TestFrame(BaseView):
    hidden = False

    def __init__(self,controller):
        super(TestFrame,self).__init__(controller)
        self.frame_path = "views/json/test_frame.json"

    def method_part(self):
        self.easy.import_methods({"go_back":self.go_back,"take_photo":self.take_photo})

    def frame_part(self):
        self.set_font([Label, Button, Entry])
        self.hide_widgets()

    def go_back(self,widgets):
        btn = self.get("ButtonBack")
        btn["command"]  = lambda window="MainFrame": self.controller.switch_window(window)

    def tkraise(self):
        self.get("root").geometry("1050x453")
        self.get("root").update()
        self.get("Frame1").tkraise()
        self.hide_widgets()
        self.controller.refresh_testing()

    def take_photo(self,widgets):
        self.get("ButtonCheck")["command"] = self.controller.test_picture

    def hide_widgets(self):
        editing_type = self.half_time.editing_type
        if editing_type in ("first_regular", "second_regular") and self.hidden == False:
            self.hidden = True
            if editing_type == "first_regular":
                self.get("LabelSecondHalf").grid_remove()
                self.get("LabelMessageSecondHalf").grid_remove()
            else:
                self.get("LabelFirstHalf").grid_remove()
                self.get("LabelMessageFirstHalf").grid_remove()
            for i in (3, 4, 5):
                self.get("HalfTimeTestLabel").grid_remove()
                self.get("RadiobuttonFirst").grid_remove()
                self.get("RadiobuttonSecond").grid_remove()