from tkinter import *
from easy_tkinter import Easy
import threading
import datetime


class HighlightsFrame(Frame):
    current_half_time = 0
    other_data_counter = 0
    other_data = {}
    label_set = False

    def __init__(self, parent, controller, models):
        Frame.__init__(self, parent)
        # set model
        self.all_highlights = models["AllHighlights"]
        self.half_time = models["AllHalfTime"]
        #first_regular

        # root controllers for switching pages
        self.controller = controller
        self.grid(row=0, column=0, sticky=W)
        self.scrollbar_setup()
        self.create_widgets()

        # self.current_editing_type = input(">>>")
        self.set_keypress()

    def set_keypress(self):
        for i in ["<Tab>", "q", "Q", "f", "F"]:
            self.controller.bind(i, self.__keypress)

    def create_widgets(self):
        self.add_back_button()

    def set_first_highlights_label(self):
        if self.label_set == False:
            self.label_set = True
            if self.half_time.editing_type in ("first_regular", "full_regular"):
                self.check_highlights_label("FIRST HALF:")
            else:
                self.check_highlights_label("SECOND HALF:")

    def scrollbar_setup(self):
        self.canvas = Canvas(self, borderwidth=0)
        self.frame = Frame(self.canvas)
        self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.easy = Easy(self.frame)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def add_back_button(self):
        # 0 1
        self.easy.set_font(("Courier", 20))
        self.easy.insert(Button, 0, self.easy.set_data(text="<", padx=(5, 2), pady=5))
        self.easy.set("command", lambda frame="MainFrame": self.controller.prebaci_frejm(frame))

    def getLista(self):
        return self.all_highlights.get_last_row()

    def add_row(self):
        self.other_data_counter += 1
        self.all_highlights.create_row()
        other_data = []
        self.easy.add_new_row(0)
        # 0 2
        self.easy.insert(Label, 0, self.easy.set_data(text="start", padx=(5, 2), pady=5))
        other_data.append(self.easy.get_last_children(0))
        # 0 3
        self.easy.set_font(("Courier", 20))
        self.easy.insert(Entry, 0, self.easy.set_data(" ", padx=(5, 2), pady=5))
        self.easy.set("width", 2)
        self.all_highlights.add_to_row(self.easy.get_last_children(0))
        # 0 4
        self.easy.insert(Label, 0, self.easy.set_data(text=":", pady=5))
        other_data.append(self.easy.get_last_children(0))
        # 0 5
        self.easy.insert(Entry, 0, self.easy.set_data(" ", padx=(2, 5), pady=5))
        self.easy.set("width", 2)
        self.all_highlights.add_to_row(self.easy.get_last_children(0))
        # 0 6
        self.easy.insert(Label, 0, self.easy.set_data(text="+", pady=5))
        other_data.append(self.easy.get_last_children(0))
        # 0 7
        self.easy.insert(Entry, 0, self.easy.set_data(" ", padx=(5, 20), pady=5))
        self.easy.set("width", 2)
        self.all_highlights.add_to_row(self.easy.get_last_children(0))

        self.easy.insert(Button, 0, self.easy.set_data("Delete"))
        self.easy.set("half_time", self.current_half_time)
        self.easy.set("command", lambda index=self.other_data_counter: self.deleteRow(index))

        other_data.append(self.easy.get_last_children(0))
        self.other_data.setdefault(self.other_data_counter,other_data)
        self.update()
        self.canvas.yview_moveto(2)
        self.update()

    def deleteRow(self, index):
        self.all_highlights.delete_row(index)
        for i in self.other_data[index]:
            i.destroy()
            i = None
        del self.other_data[index]

    def check_highlights_label(self, text):

        def add_highlights_label(half_time):
            self.easy.add_new_row(0)
            self.easy.insert(Label, 0, self.easy.set_data(text, pady=3, columnspan=5))
            self.current_half_time = half_time
            self.add_row()

        if text == "FIRST HALF:":
            self.all_highlights.half_time = 1
            add_highlights_label(1)
        elif text == "SECOND HALF:":
            self.all_highlights.half_time = 2
            add_highlights_label(2)

    def __keypress(self, event):
        dict_data = event.__dict__
        if self.controller.page_name == "HighlightsFrame":
            keysum = dict_data["keysym"]
            if (keysum == "Tab"):
                self.__check_data_for_tab()
            elif (keysum == "q" or "Q"):
                if self.half_time.editing_type == "full_regular":
                    if self.current_half_time < 2:
                        self.check_highlights_label("SECOND HALF:")
            elif (keysum == "f" or "F"):
                self.add_row()

    def __startFocus(obj):
        obj.t_focus = threading.Thread(target=obj.getLista()[0].focus)
        obj.t_focus.start()

    def __check_data_for_tab(self):
        last_row = self.all_highlights.get_last_row()
        counter = 0
        for i in last_row:
            if len(i.get()) > 0:
                counter += 1
        if counter == 3:
            self.add_row()
            self.__startFocus()
