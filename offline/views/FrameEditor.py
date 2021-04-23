from views.BaseView import BaseView
from easy_tk import WindowScrollbar
from views.TimeInput import TimeInput

import json
import requests
import random

class FrameEditor(BaseView):
    
    def __init__(self):
        super(FrameEditor,self).__init__()
        self.frame_path = "views/json/scrollbar.json"
        self.tab_text = "Editor"
        self.name = "FrameContainer"
        self.window_scrollbar = WindowScrollbar(self)
    
    def method_part(self):
        self.import_methods({"set_scrollbar":self.window_scrollbar.set_scrollbar})
        self.import_modules([TimeInput,])

    def download_highlights(self):
        self.model.get_highlights()

    def change_fields(self):
        for row in self.model['highlights']:
            self.add_row(row)

    def filter_halftime(self):
        for row in self.model['highlights']:
            if row['editing'] == self.model['compDesc']['editing']:
                self.get(f'Frame{row["id"]}').grid()
            else:
                self.get(f'Frame{row["id"]}').grid_remove()

    def frame_part(self):
        super().frame_part()
        
    def add_row(self,row):
        self.open_file("views/json/highlights.json")
        self.easy.change_frame_key('ID', str(row['id']))
        self.reading_from_json()
        self.add_model_to_row(row)
        self.insert_in_row(row)
        self.add_listeners(row)
        self.get(f'TimeInputMin{row["id"]}').focus()      
    
    def add_model_to_row(self,row):
        self.get(f'TimeInputMin{row["id"]}').set_model(row,"min")
        self.get(f'TimeInputSec{row["id"]}').set_model(row,"sec")
        self.get(f'TimeInputToAdd{row["id"]}').set_model(row,"toAdd")

    def add_listeners(self,row):
         self.get(f'TimeInputToAdd{row["id"]}').bind("<Tab>",lambda a=5 : self.tab_pressed())
         self.get(f'ButtonDelete{row["id"]}')['command'] = lambda row=row: self.delete_row(row)

    def delete_row(self,row):
        for i in list(self.easy.all_widgets.keys()):
            if i.endswith(str(row['id'])):
                self.easy.remove_widget(i)
        self.model.remove_row(row)
        self.model.post_highlights()

    def tab_pressed(self):
        for i in self.model['highlights']:
            if i['editing'] == self.model['compDesc']['editing']:
                if i['min'] and i['sec'] and i['toAdd'] not in [None,""]:
                    can_add = True
                else:
                    can_add = False
                    break
        if can_add == True:
            row = {'min':None,'sec':None,'toAdd':None,'editing':self.model['compDesc']['editing'],'id':self.model.new_id()}
            self.model['highlights'].append(row)
            self.add_row(row)
            self.model.post_highlights()

    def insert_in_row(self,row):
        self.get(f'TimeInputMin{row["id"]}').insert(0,row['min'])
        self.get(f'TimeInputSec{row["id"]}').insert(0,row['sec'])
        self.get(f'TimeInputToAdd{row["id"]}').insert(0,row['toAdd'])