from easy_tk import EasyTkObject
from tkinter import Label,Button,Entry

class TestFrame(EasyTkObject):
    hidden = False

    def __init__(self, root, widget,controller,set_font):
        super(TestFrame, self).__init__()
        self.easy.add_complete_widget(root)
        self.easy.add_complete_widget(widget)
        self.controller = controller
        self.set_font = set_font

    def set_models(self,models):
        self.match = models["Match"]
        self.half_time = models["AllHalfTime"]
        self.videos = models["Videos"]
        self.all_highlights = models["AllHighlights"]

    def go_back(self,widgets):
        btn = self.get("ButtonBack")
        btn["command"]  = lambda window="MainFrame": self.controller.switch_window(window)

    def create_widgets(self):
        self.easy.import_methods([self.go_back,self.take_photo])
        self.open_file("views/json/test_frame.json")
        self.reading_from_json()
        self.set_font(self.easy.all_widgets, [Label, Button, Entry])
        self.hide_widgets()

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