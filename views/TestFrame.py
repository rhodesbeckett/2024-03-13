import os
import warnings
from tkinter import *
from tkinter.ttk import Separator
from easy_tkinter import Easy
import cv2
from PIL import Image, ImageTk
import datetime


class TestFrame(Frame):
    check_messages = {}
    tested = False
    ceo_mec_sekunde = 0

    def __init__(self, parent, controller,models):
        Frame.__init__(self, parent)
        self.easy = Easy(self)
        self.easy.set_font(("Courier", 20))
        # set all models
        self.match = models["Match"]
        self.half_time = models["AllHalfTime"]
        self.videos = models["Videos"]
        self.all_highlights = models["AllHighlights"]
        # root controllers for switching pages
        self.controller = controller
        self.grid(row=0, column=0, sticky=W)
        self.create_widgets()

    def create_widgets(self):
        # 0 0
        # font=("Courier", 20)
        data = self.easy.set_data("<", padx=(5, 0), pady=5, sticky=W)
        self.easy.insert(Button, 0, data)
        self.easy.set("command", lambda var="MainFrame": self.controller.prebaci_frejm(var), 0, 0)
        self.easy.add_new_row(0)
        # 0 1
        data = self.easy.set_data("MATCH", padx=(5, 0), pady=0, sticky=W)
        self.easy.insert(Label, 0, data)
        # 0 2
        data = self.easy.set_data(" ", columnspan=3, sticky=E)
        self.easy.insert(Label, 0, data)
        self.check_messages.setdefault("MATCH",self.easy.get_last_children(0))
        self.easy.add_new_row(0)
        # 0 3
        data = self.easy.set_data("First half", padx=(5, 0), pady=0, sticky=W)
        self.easy.insert(Label, 0, data)
        # 0 4
        data = self.easy.set_data("NOT OK", padx=(0, 0), pady=0, columnspan=3, sticky=E)
        self.easy.insert(Label, 0, data)
        self.check_messages.setdefault("First half",self.easy.get_last_children(0))
        self.easy.add_new_row(0)
        # 0 5
        data = self.easy.set_data("Second half", padx=(5, 0), pady=0, sticky=W)
        self.easy.insert(Label, 0, data)
        # 0 6
        data = self.easy.set_data("NOT OK", padx=0, pady=0, columnspan=3, sticky=E)
        self.easy.insert(Label, 0, data)
        self.check_messages.setdefault("Second half",self.easy.get_last_children(0))
        self.easy.add_new_row(0)
        # 0 7
        data = self.easy.set_data("Enter timestamp for testing:", padx=(5, 0), pady=0, columnspan=3, sticky=W)
        self.easy.insert(Label, 0, data)
        self.easy.add_new_row(0)

        self.addEntriesTestFrame()

        # 0 9
        data = self.easy.set_data(None, rowspan=10, sticky=NS)
        self.easy.insert(Separator, 0, data)
        self.easy.set("orient", VERTICAL, 0, 9)
        self.easy.set_specific_grid(0, 9, 0, 5)
        # 0 10
        self.addTestPhoto()
        # 0 11
        self.easy.add_new_row(0)
        data = self.easy.set_data("Highlights:", padx=(5, 0), sticky=W, columnspan=3)
        self.easy.insert(Label, 0, data)
        # self.tkw.addNewRow(0)
        # # 0 12
        data = self.easy.set_data("NOT OK", padx=(5, 0), columnspan=2, sticky=E)
        self.easy.insert(Label, 0, data)
        self.check_messages.setdefault("Highlights",self.easy.get_last_children(0))

    def addEntriesTestFrame(self):
        # 0 8
        data = self.easy.set_data("", sticky=W)
        self.easy.insert(Frame, 0, data, True)

        # 1 0
        data = self.easy.set_data(" ", padx=(5, 2), pady=7, sticky=W)
        self.easy.insert(Entry, 1, data)
        self.easy.set("width", 2, 1, 0)
        # 1 1
        data = self.easy.set_data(":", padx=(0, 5), pady=5, sticky=W)
        self.easy.insert(Label, 1, data)
        # 1 2
        data = self.easy.set_data(" ", padx=(2, 5), pady=2, sticky=W)
        self.easy.insert(Entry, 1, data)
        self.easy.set("width", 2, 1, 2)
        # 1 3
        data = self.easy.set_data("Halftime:", sticky=W)
        self.easy.insert(Label, 1, data)

        self.poluvremeVar = StringVar()
        self.poluvremeVar.set("prvo")
        # 1 4
        data = self.easy.set_data("1", padx=2, sticky=W, columnspan=1)
        self.easy.insert(Radiobutton, 1, data)
        self.easy.set("value", "prvo", 1, 4)
        self.easy.set("variable", self.poluvremeVar, 1, 4)
        # 1 5
        data = self.easy.set_data("2", columnspan=1, sticky=W, padx=2)
        self.easy.insert(Radiobutton, 1, data)

        self.easy.set("value", "drugo", 1, 5)
        self.easy.set("variable", self.poluvremeVar, 1, 5)

        # 1 6
        self.easy.add_new_row(1)

        data = self.easy.set_data("Check", columnspan=3, sticky=W, padx=(5, 0))
        self.easy.insert(Button, 1, data)
        self.easy.set("command",self.take_photo)
        self.easy.set("font", ("Courier", 12), 1, 6)

    def addTestPhoto(self):
        # 0 10
        data = self.easy.set_data("", rowspan=10, padx=10, pady=10, sticky=NW, row=0, column=7)
        self.easy.insert(Label, 0, data)

    def hide_widgets(self):
        editing_type = self.half_time.editing_type
        if editing_type in ("first_regular","second_regular"):
            if editing_type == "first_regular":
                self.easy.set("grid_remove",None,0,5)
                self.easy.set("grid_remove", None, 0, 6)
            else:
                self.easy.set("grid_remove", None, 0, 3)
                self.easy.set("grid_remove", None, 0, 4)
            for i in (3,4,5):
                self.easy.set("grid_remove",None,1,i)

    def take_photo(self):
        self.controller.test_picture()