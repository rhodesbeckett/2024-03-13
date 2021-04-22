from views.BaseView import BaseView
from views.TimeInput import TimeInput
import requests
import json

class FrameMatchInfo(BaseView):

    def __init__(self):
        super(FrameMatchInfo,self).__init__()
        self.frame_path = "views/json/matchInfo.json"
        self.json_frame = "FrameMatchInfo"
        self.tab_text = "MatchInfo"
        self.ID = ""
    
    def method_part(self):
        self.import_variables({'saveBtn':self.save_match_info})
        self.import_modules([TimeInput,])

    def download_match_comp(self,ID,halftime):
        self.ID = ID
        res = requests.get(f'http://localhost:5000/getMC/{ID}')
        self.comp_desc = json.loads( res.json()['compDesc'] )
        self.comp_desc['editing'] = halftime
        self.comp_desc['time']['isChosen'] = True
        requests.post(f'http://localhost:5000/update/{self.ID}/compDesc',json.dumps(self.comp_desc))

    def change_fields(self):
        self.change_title()
        self.change_src()
        self.add_model_to_row()
        self.change_halftime()
        self.show_halftime()

    def change_title(self):
        self.get('EntryTitle').delete(0,'end')
        title = self.comp_desc['title'] if self.comp_desc['title'] != "" else ""
        self.get('EntryTitle').insert(0,self.comp_desc['title'])
    
    def change_src(self):
        self.get('EntryMatch').delete(0,'end')
        self.get('EntryMatch').insert(0,self.comp_desc['src'])

    def change_halftime(self):
        for entry in ['TimeInputFirstHalfMin','TimeInputFirstHalfSec','TimeInputSecondHalfMin','TimeInputSecondHalfSec']:
            self.get(entry).delete(0,'end')
        
        self.get('TimeInputFirstHalfMin').insert(0,self.comp_desc['time']['firstHalf']['min'])
        self.get('TimeInputFirstHalfSec').insert(0,self.comp_desc['time']['firstHalf']['sec'])
        self.get('TimeInputSecondHalfMin').insert(0,self.comp_desc['time']['secondHalf']['min'])
        self.get('TimeInputSecondHalfSec').insert(0,self.comp_desc['time']['secondHalf']['sec'])
        
    def add_model_to_row(self):
        self.get('TimeInputFirstHalfMin').set_model(self.comp_desc['time']['firstHalf'],'min')
        self.get('TimeInputFirstHalfSec').set_model(self.comp_desc['time']['firstHalf'],'sec')
        self.get('TimeInputSecondHalfMin').set_model(self.comp_desc['time']['secondHalf'],'min')
        self.get('TimeInputSecondHalfSec').set_model(self.comp_desc['time']['secondHalf'],'sec')

    def save_match_info(self):
        self.comp_desc['title'] = self.get('EntryTitle').get()
        """ self.comp_desc['src'] = "" """
        requests.post(f'http://localhost:5000/update/{self.ID}/compDesc',json.dumps(self.comp_desc))

    def show_halftime(self):
        if self.comp_desc['editing'] == "firstHalf":
            self.get('FrameSecondHalf').grid_remove()
            self.get('FrameFirstHalf').grid()
        else:
            self.get('FrameFirstHalf').grid_remove()
            self.get('FrameSecondHalf').grid()