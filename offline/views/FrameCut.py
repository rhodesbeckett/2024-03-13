from views.BaseView import BaseView
from tkinter.ttk import Progressbar
class FrameCut(BaseView):

    def __init__(self):
        super(FrameCut,self).__init__()
        self.frame_path = "views/json/cut.json"
        self.json_frame = "FrameCut"
        self.tab_text = "Cut"
        
    def method_part(self):
        self.import_modules([Progressbar,])