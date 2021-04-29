from views.BaseView import BaseView
from tkinter.ttk import Progressbar
import requests
import json

class FrameRender(BaseView):

    def __init__(self):
        super(FrameRender,self).__init__()
        self.frame_path = "views/json/render.json"
        self.json_frame = "FrameRender"
        self.tab_text = "Render"
    
    def method_part(self):
        self.import_variables({"render":self.render,})
        self.import_modules([Progressbar,])

    def render(self):
        if self.model['canCut'] == True:
            requests.get(f'http://localhost:5000/render/{self.model["id"]}')