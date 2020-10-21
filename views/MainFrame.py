from tkinter import *
from easy_tkinter import Easy
from tkinter import filedialog, messagebox


class MainFrame(Frame):

    def __init__(self, parent, controller, models):
        Frame.__init__(self, parent)
        self.easy = Easy(self)
        # set all models
        self.match = models["Match"]
        self.half_time = models["AllHalfTime"]
        self.videos = models["Videos"]
        self.all_highlights = models["AllHighlights"]

        # root controllers for switching pages
        self.controller = controller
        self.create_widgets()
        self.adding_commands()

    def create_widgets(self):
        self.easy.set_font(("Courier", 20))
        self.easy.insert(Button, 0, self.easy.set_data("MATCH", 15, 5))
        self.easy.insert(Button, 0, self.easy.set_data("HIGHLIGHTS", 15, 5, ))

        self.easy.insert(Frame, 0, self.easy.set_data(None), True)

        self.easy.insert(Label, 1, self.easy.set_data("FIRST HALF:", 0, 5, E))

        self.easy.insert(Entry, 1, self.easy.set_data(" ", (5, 2), 5, E))
        self.easy.set("width", 2)

        self.easy.insert(Label, 1, self.easy.set_data(":", (0, 0), 5, E))

        self.easy.insert(Entry, 1, self.easy.set_data(" ", (5, 2), 5, E))
        self.easy.set("width", 2)

        self.easy.insert(Label, 1, self.easy.set_data("SECOND HALF:", (0, 0), 5, E))
        self.easy.insert(Entry, 1, self.easy.set_data(" ", (5, 2), 5, E))
        self.easy.set("width", 2)

        self.easy.insert(Label, 1, self.easy.set_data(":", pady=5, sticky=E))

        self.easy.insert(Entry, 1, self.easy.set_data(" ", (2, 5), 5, E))
        self.easy.set("width", 2)

        self.easy.add_new_row(0)

        self.easy.insert(Button, 0, self.easy.set_data("TEST", 15, 5, W))
        self.easy.insert(Button, 0, self.easy.set_data("RUN", 15, 5, W))

        self.easy.insert(Frame, 0, self.easy.set_data(None), True)
        # , 15, 5, E
        self.easy.insert(Button, 2, self.easy.set_data("JUST CUT", 1, 5, W))
        self.easy.insert(Label, 2, self.easy.set_data("FOLDER:", 15, 5, E))
        self.easy.insert(Entry, 2, self.easy.set_data(" ", 15, 5, E))

    def open_match_src(self):
        rep = filedialog.askopenfilename(
            title="Load file",
            parent=self,
            initialdir='/adffgdfg',
            initialfile='tmp',
            filetypes=[
                ("All files", "*")])
        self.match.set_match(rep)
        self.controller.refresh_testing()

    def adding_commands(self):
        self.easy.set("command", self.open_match_src, 0, 0)
        self.easy.set("command", lambda frame="HighlightsFrame": self.controller.prebaci_frejm(frame), 0, 1)
        self.easy.set("command", self.start_test, 0, 3)
        self.easy.set("command", self.controller.render, 0, 4)
        self.easy.set("command", self.controller.cut, 2, 0)
        self.click_on_entries()

    def click_on_entries(self):
        parent = 1
        for i in [1,3,5,7,2]:
            if i == 2:
                parent = 2
            self.easy.get_object(parent,i).bind("<1>",lambda a=5:self.controller.refresh_testing())

    def start_test(self):
        self.half_time.set_time(self.get_half_time(1))
        self.half_time.set_time(self.get_half_time(2))
        self.videos.set_src(self.get_video())
        self.controller.prebaci_frejm("TestFrame")

    def hide_half_time(self):
        # provera novog modula halftimes
        if self.half_time.editing_type == "first_regular":
            self.easy.set("state", "disabled", 1, 5)
            self.easy.set("state", "disabled", 1, 7)

        elif self.half_time.editing_type == "second_regular":
            self.easy.set("state", "disabled", 1, 1)
            self.easy.set("state", "disabled", 1, 3)

    def get_half_time(self, half_time):
        if half_time == 1:
            return (self.easy.get_text(1, 1), self.easy.get_text(1, 3))
        elif half_time == 2:
            return (self.easy.get_text(1, 5), self.easy.get_text(1, 7))

    def get_video(self):
        return self.easy.get_text(2, 2)
