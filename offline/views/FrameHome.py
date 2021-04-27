from views.BaseView import BaseView
import requests
import json
from tkinter import StringVar

class FrameHome(BaseView):
    
    def __init__(self):
        super(FrameHome,self).__init__()
        self.frame_path = "views/json/home.json"
        self.json_frame = "FrameHome"
        self.tab_text = "Home"
        self.query_get_all = "http://localhost:5000/getAll"
    
    def frame_part(self):
        super().frame_part()
        res = requests.get(self.query_get_all)
        self.all_comps = json.loads( res.json()['allComps'] )
        for comp in self.all_comps:
            self.add_comp(comp)

    def add_comp(self,comp):
        string_var = StringVar(self.get('root'),'firstHalf')
        self.import_variables({f'string_var{comp["_id"]["$oid"]}':string_var,
        'clickRadio1':lambda ID=comp["_id"]["$oid"], halftime="firstHalf" : self.controller.switch_to_editor(ID,halftime),
        'clickRadio2':lambda ID=comp["_id"]["$oid"],halftime="secondHalf" : self.controller.switch_to_editor(ID,halftime),
        "mergeBtn":lambda ID=comp["_id"]["$oid"]: self.mergeBtn(ID) })
        self.open_file("views/json/compCard.json")
        self.easy.change_frame_key('ID', comp['_id']['$oid'])
        self.easy.change_frame_key('TITLE', comp['compDesc']['title'])
        self.reading_from_json()

    def mergeBtn(self,ID):
        req = requests.get(f'http://localhost:5000/mergeVideos/{ID}')
        print(req.json())
