from easy_tk import EasyTkObject
from tkinter import Label,Button
from PIL import ImageTk,Image
class ChoiceFrame(EasyTkObject):

    def __init__(self, root, widget,controller,set_font):
        super(ChoiceFrame, self).__init__()
        self.easy.add_complete_widget(root)
        self.easy.add_complete_widget(widget)
        self.controller = controller
        self.set_font = set_font

    def set_models(self,models):
        self.all_half_time = models["AllHalfTime"]

    def create_widgets(self):
        self.open_file("views/json/choice_frame.json")

    def tkraise(self):
        self.easy.import_methods({"btn":self.btn})
        self.reading_from_json()
        self.easy.all_widgets.get("root").get().geometry("1035x453")
        self.easy.all_widgets.get("root").get().update()
        self.easy.all_widgets.get("Frame2").get().tkraise()
        self.set_font(self.easy.all_widgets,[Label,Button])
        self.imeage = ImageTk.PhotoImage(Image.open("bg.gif"))
        self.get("LabelBackground")["image"] = self.imeage

    def choose(self,choice):
        self.all_half_time.set_editing_type(choice)
        self.controller.switch_window("MainFrame")
        self.controller.prozori["MainFrame"].hide_entry()
        self.controller.prozori["HighlightsFrame"].set_first_highlights_label()
        self.controller.prozori.pop("ChoiceFrame")


    def btn(self,widgets):
        counter = -1
        for i in widgets:
            if i.startswith("Button"):
                counter+=1
                text = self.all_half_time.choices[counter]
                self.get(i)["command"] = lambda choice=text:self.choose(choice)
                self.get(i)["relief"] = "solid"
                self.get(i)["borderwidth"] = 2
                self.get(i)["bg"] = "#dedcdc"