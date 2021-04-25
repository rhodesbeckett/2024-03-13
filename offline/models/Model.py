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
        self['test'] = {
                "src":False,
                "halfTime":False,
                "highlights":False
        }
        self['canCut'] = False
        self['canRender'] = False
        self['cutProgress'] = 0
        self['renderProgress'] = 0
        self['id'] = None
        self['toRemove'] = False
        self.change_dir()
    
    #add/update/remove

    def get_mc(self,ID):
        self['id'] = ID
        res = requests.get(f'http://localhost:5000/getMC/{ID}')
        self['compDesc'] = json.loads( res.json()['compDesc'] )

    def get_highlights(self):
        res = requests.get(f'http://localhost:5000/getHighlights/{self["id"]}')
        self['highlights'] = json.loads( res.json()['highlights'] )

    def get_testing(self):
        res = requests.get(f'http://localhost:5000/getTesting/{self["id"]}')
        self['testing'] = json.loads( res.json()['testing'] )
    
    def test_img(self,test_data):
        res = requests.get(f'http://localhost:5000/getPhoto/{test_data["min"]}/{test_data["sec"]}')
        return res.json()['imgSrc']
    
    def update_editing(self,halftime):
        self['compDesc']['editing'] = halftime
        self['compDesc']['time']['isChosen'] = True

    def update_title(self,title):
        self['compDesc']['title'] = title

    def update_src(self,src):
        self['compDesc']['src'] = src

    def remove_row(self,row):
        self['highlights'].remove(row)

    def update_id(self,id):
        self['id'] = id
    
    def update_to_remove(self,to_remove):
        self['toRemove'] = to_remove
        
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
    
    def change_dir(self):
        requests.get('http://localhost:5000/changeDir')