from easy_tk.helpers import *
from easy_tk import WindowScrollbar
from tkinter import Label, Button, Entry
import threading
from PIL import ImageTk,Image
from views.BaseView import BaseView

keys = ["LabelStart", "EntryStart", "LabelColon", "EntrySecStart", "LabelPlus", "EntrySecEnd", "ButtonDelete"]


class HighlightsFrame(BaseView):
    current_half_time = 0
    label_set = False

    def __init__(self,controller):
        super(HighlightsFrame,self).__init__(controller)
        self.window_scrollbar = WindowScrollbar(self)
        self.frame_path = "views/json/scrollbar.json"

    def set_models(self, models):
        self.all_highlights = models["AllHighlights"]
        self.half_time = models["AllHalfTime"]
        self.other_widgets = {}
        self.all_highlights.set_names(keys)

    def method_part(self):
        methods = {"set_scrollbar":self.window_scrollbar.set_scrollbar,
        "go_back":self.go_back,
        "set_keypresss":self.set_keypress}
        self.easy.import_methods(methods)

    def frame_part(self):
        self.open_file("views/json/highlights_frame_1.json")
        self.reading_from_json()

        self.add_row()
        self.add_to_all_highlights()
        # self.set_first_highlights_label()

        self.image = ImageTk.PhotoImage(Image.open("bg.gif"))
        self.get("LabelBackground")["image"] = self.image
        
        self.frame_to_raise="Frame0"
        self.dimensions="562x467"

    def add_row(self):
        self.open_file("views/json/highlights_frame_2.json")
        self.reading_from_json()
        self.set_font([Label, Button, Entry])
        self.all_highlights.create_row()

    def add_to_all_highlights(self):
        row = self.all_highlights.current_row
        def sufix():
            if row == 1:
                br = ""
            else:
                br = "_{}".format(row)
            return br

        other_widgets = []
        br = sufix()
        for i in keys:
            i = "{}{}".format(i,br)
            if i.startswith("Entry"):
                self.all_highlights.add_to_row(self.get(i))
            else:
                other_widgets.append(self.get(i))
        other_widgets[-1]["command"] = lambda br=row:self.delete_row(br)
        self.other_widgets.setdefault(self.all_highlights.current_row,other_widgets)


    def go_back(self, widgets):
        btn = self.get("ButtonBack")
        btn["command"] = lambda window="MainFrame": self.controller.switch_window(window)

    def set_keypress(self, widgets):
        for i in ["<Tab>", "q", "Q", "f", "F"]:
            self.get("root").bind(i, self.__keypress)

    def __keypress(self, event):
        dict_data = event.__dict__
        if self.controller.page_name == "HighlightsFrame":
            keysum = dict_data["keysym"]
            if keysum == "Tab":
                self.__check_data_for_tab()
            elif keysum in ("q", "Q"):
                if self.half_time.editing_type == "full_regular":
                    if self.current_half_time < 2:
                        self.check_highlights_label("SECOND HALF:")
            elif keysum in ("f", "F"):
                self.add_row()
                self.add_to_all_highlights()
                # self.add_row()

    def __check_data_for_tab(self):
        last_row = self.all_highlights.get_last_row()
        counter = 0
        for i in last_row:
            if len(i.get()) > 0:
                counter += 1
        if counter == 3:
            self.add_row()
            self.add_to_all_highlights()
            self.__startFocus()

    def __startFocus(obj):
        obj.t_focus = threading.Thread(target=obj.getLista()[0].focus)
        obj.t_focus.start()

    def delete_row(self, index):
        self.all_highlights.delete_row(index)
        for i in self.other_widgets[index]:
            i.destroy()
            i = None
        del self.other_widgets[index]

    def set_first_highlights_label(self):
        if self.label_set == False:
            self.label_set = True
            if self.half_time.editing_type in ("first_regular", "full_regular"):
                self.check_highlights_label("FIRST HALF:")
            else:
                self.check_highlights_label("SECOND HALF:")

    def check_highlights_label(self, text):

        def add_highlights_label(half_time):
            self.get("LabelHalfTime")["text"] = text
            self.current_half_time = half_time

        if text == "FIRST HALF:":
            self.all_highlights.half_time = 1
            add_highlights_label(1)
        elif text == "SECOND HALF:":
            self.all_highlights.half_time = 2
            add_highlights_label(2)

    def getLista(self):
        return self.all_highlights.get_last_row()

    def tkraise(self):
        super(HighlightsFrame,self).tkraise()
        self.controller.refresh_testing()
