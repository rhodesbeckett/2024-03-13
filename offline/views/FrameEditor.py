from views.BaseView import BaseView
from easy_tk import WindowScrollbar
from views.TimeInput import TimeInput

import json
import requests

class FrameEditor(BaseView):
    
    def __init__(self):
        super(FrameEditor,self).__init__()
        self.frame_path = "views/json/scrollbar.json"
        self.tab_text = "Editor"
        self.name = "FrameContainer"
        self.window_scrollbar = WindowScrollbar(self)
        self.ID = ""
        self.halftime = ""
    
    def method_part(self):
        self.import_methods({"set_scrollbar":self.window_scrollbar.set_scrollbar})
        self.import_modules([TimeInput,])

    def frame_part(self):
        self.add_row()
        self.add_row()
        self.add_row()
        self.add_row()
        super().frame_part()
        
    
    def add_row(self):
        self.open_file("views/json/highlights.json")
        #changes
        self.reading_from_json()

    def change_halftime(self,ID,halftime):
        print(ID)
        print(halftime)

    def change_fields(self):
        pass