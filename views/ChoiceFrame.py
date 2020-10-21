from tkinter import *
from easy_tkinter import Easy
class ChoiceFrame(Frame):
    question = "How you want to edit videos?"

    def __init__(self, parent, controller, models):
        Frame.__init__(self, parent)
        self.controller = controller
        self.all_half_time = models["AllHalfTime"]
        self.easy = Easy(self)
        self.create_widgets()

    def create_widgets(self):
        # napravi label za pitanje
        self.easy.insert(Label,0,self.easy.set_data(self.question,(50,5),5,columnspan=3))
        self.easy.set("font",("Helvetica",20))
        # napravi dugmad
        self.easy.add_new_row(0)
        for i in self.all_half_time.choices:
            choice = self.all_half_time.choices[i]
            self.easy.insert(Button,0,self.easy.set_data(i,10,10))
            self.easy.set("command",lambda choice=choice:self.choose(choice))

    def choose(self,choice):
        self.all_half_time.set_editing_type(choice)
        self.controller.prebaci_frejm("MainFrame")