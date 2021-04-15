from views.BaseView import BaseView
from tkinter.ttk import Progressbar

class FrameRender(BaseView):

    def __init__(self):
        super(FrameRender,self).__init__()
        self.frame_path = "views/json/render.json"
        self.json_frame = "FrameRender"
        self.tab_text = "Render"
    
    def method_part(self):
        self.import_modules([Progressbar,])