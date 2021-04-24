from views.BaseView import BaseView
from views import TimeInput

class FrameTest(BaseView):
    
    def __init__(self):
        super(FrameTest,self).__init__()
        self.frame_path = "views/json/testing.json"
        self.json_frame = "FrameTest"
        self.tab_text = "Testing"
        self.time_data = {'min':None,'sec':None}

    def method_part(self):
        self.import_modules([TimeInput,])
        self.import_variables({'test_img':self.test_img})

    def test_img(self):
        self.model.test_img(self.time_data)

    def frame_part(self):
        super().frame_part()
        self.get('TimeInputMin').set_model(self.time_data,'min')
        self.get('TimeInputSec').set_model(self.time_data,'sec')
    
    def download_testing(self):
        if self.model['id'] != None:
            self.model.get_testing()
            self.change_fields()

    def change_fields(self):
        color = ""
        for key,value in self.model['testing'].items():
            if value == True:
                color = "red" if color == "red" else "green"
                self.get(f'LabelResponse{key.capitalize()}')['bg'] = color
            else:
                color = "red"
                self.get(f'LabelResponse{key.capitalize()}')['bg'] = color

