import requests
import json
import random

class Model(dict):
    counter = 0
    def __init__(self):
        super().__init__(self)
        self["compDesc"] = {
        "title": "",
        "src": "",
        "editing": "",
        "time": {
            "isChosen": False,
            "firstHalf": {"min": None,"sec":None},
            "secondHalf": {"min": None,"sec":None}
            }
        }
        self['highlights'] = []
        self['testing'] = {
                "src":False,
                "halfTime":False,
                "highlights":False
        }
        self['canCut'] = False
        self['canRender'] = False
        self['cutProgress'] = 0
        self['renderProgress'] = 0
        self['id'] = None
    
    #add/update/remove

    def get_mc(self,ID):
        self['id'] = ID
        res = requests.get(f'http://localhost:5000/getMC/{ID}')
        self['compDesc'] = json.loads( res.json()['compDesc'] )

    def get_highlights(self):
        res = requests.get(f'http://localhost:5000/getHighlights/{self["id"]}')
        self['highlights'] = json.loads( res.json()['highlights'] )
    
    def update_editing(self,halftime):
        self['compDesc']['editing'] = halftime
        self['compDesc']['time']['isChosen'] = True

    def update_title(self,title):
        self['compDesc']['title'] = title

    def update_src(self,src):
        self['compDesc']['src'] = src

    def remove_row(self,row):
        self['highlights'].remove(row)

    #post

    def post_mc(self):
        requests.post(f'http://localhost:5000/update/{self["id"]}/compDesc',json.dumps(self['compDesc']))
    
    def post_highlights(self):
        requests.post(f'http://localhost:5000/update/{self["id"]}/highlights',json.dumps(self['highlights']))

    #helpers
    def new_id(self):
        ids = []
        for row in self['highlights']:
            ids.append(row['id'])
        while(True):
            ID = random.randint(1,10000)
            if ID not in ids:
                return ID

