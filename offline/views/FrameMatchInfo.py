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
        self.model.get_mc(ID)
        self.model.update_editing(halftime)
        self.model.post_mc()

    def change_fields(self):
        self.change_title()
        self.change_src()
        self.add_model_to_row()
        self.change_halftime()
        self.show_halftime()

    def change_title(self):
        self.get('EntryTitle').delete(0,'end')
        title = self.model['compDesc']['title'] if self.model['compDesc']['title'] != "" else ""
        self.get('EntryTitle').insert(0,self.model['compDesc']['title'])
    
    def change_src(self):
        self.get('EntryMatch').delete(0,'end')
        self.get('EntryMatch').insert(0,self.model['compDesc']['src'])

    def change_halftime(self):
        for entry in ['TimeInputFirstHalfMin','TimeInputFirstHalfSec','TimeInputSecondHalfMin','TimeInputSecondHalfSec']:
            self.get(entry).delete(0,'end')
        
        self.get('TimeInputFirstHalfMin').insert(0,self.model['compDesc']['time']['firstHalf']['min'])
        self.get('TimeInputFirstHalfSec').insert(0,self.model['compDesc']['time']['firstHalf']['sec'])
        self.get('TimeInputSecondHalfMin').insert(0,self.model['compDesc']['time']['secondHalf']['min'])
        self.get('TimeInputSecondHalfSec').insert(0,self.model['compDesc']['time']['secondHalf']['sec'])
        
    def add_model_to_row(self):
        self.get('TimeInputFirstHalfMin').set_model(self.model['compDesc']['time']['firstHalf'],'min')
        self.get('TimeInputFirstHalfSec').set_model(self.model['compDesc']['time']['firstHalf'],'sec')
        self.get('TimeInputSecondHalfMin').set_model(self.model['compDesc']['time']['secondHalf'],'min')
        self.get('TimeInputSecondHalfSec').set_model(self.model['compDesc']['time']['secondHalf'],'sec')

    def save_match_info(self):
        self.model.update_title(self.get('EntryTitle').get())
        self.model.update_src(self.get('EntryMatch').get())
        self.model.post_mc()

    def show_halftime(self):
        if self.model['compDesc']['editing'] == "firstHalf":
            self.get('FrameSecondHalf').grid_remove()
            self.get('FrameFirstHalf').grid()
        else:
            self.get('FrameFirstHalf').grid_remove()
            self.get('FrameSecondHalf').grid()