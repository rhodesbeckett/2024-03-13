from views.BaseView import BaseView
from tkinter.ttk import Progressbar
import requests
import json

class FrameCut(BaseView):

    def __init__(self):
        super(FrameCut,self).__init__()
        self.frame_path = "views/json/cut.json"
        self.json_frame = "FrameCut"
        self.tab_text = "Cut"
        
    def method_part(self):
        self.import_variables({"cut":self.cut})
        self.import_modules([Progressbar,])
    
    def get_can_cut(self):
        req = requests.get(f'http://localhost:5000/getCanCut/{self.model["id"]}')
        self.model['canCut'] = req.json()['canCut']
    
    def cut(self):
        if self.model['canCut']:
            requests.get(f'http://localhost:5000/cut/{self.model["id"]}')

