from tkinter import Label,Button
from PIL import ImageTk,Image
from views.BaseView import BaseView

class ChoiceFrame(BaseView):
    
    def __init__(self,controller):
        super(ChoiceFrame,self).__init__(controller)
        self.frame_path = "views/json/choice_frame.json"

    def method_part(self):
        self.easy.import_methods({"btn":self.btn})

    def frame_part(self):
        self.set_font([Label,Button])
        self.image = ImageTk.PhotoImage(Image.open("bg.gif"))
        self.get("LabelBackground")["image"] = self.image
        self.frame_to_raise = "Frame2"
        self.dimensions = "1035x453"


    def choose(self,choice):
        self.half_time.set_editing_type(choice)
        self.controller.switch_window("MainFrame")
        self.controller.prozori["MainFrame"].hide_entry()
        self.controller.prozori["HighlightsFrame"].set_first_highlights_label()
        self.controller.prozori.pop("ChoiceFrame")

    def btn(self,widgets):
        counter = -1
        for i in widgets:
            if i.startswith("Button"):
                counter+=1
                text = self.half_time.choices[counter]
                self.get(i)["command"] = lambda choice=text:self.choose(choice)
                self.get(i)["relief"] = "solid"
                self.get(i)["borderwidth"] = 2
                self.get(i)["bg"] = "#dedcdc"