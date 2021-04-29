from views.BaseView import BaseView
from views import TimeInput
from PIL import Image,ImageTk

class FrameTest(BaseView):
    
    def __init__(self):
        super(FrameTest,self).__init__()
        self.frame_path = "views/json/testing.json"
        self.json_frame = "FrameTest"
        self.tab_text = "Testing"
        self.time_data = {'min':None,'sec':None}
        self.addr = "http://localhost:5000"

    def method_part(self):
        self.import_modules([TimeInput,])
        self.import_variables({'test_img':self.test_img})

    def test_img(self):
        url = self.model.test_img(self.time_data)
        self.test_img = ImageTk.PhotoImage(Image.open(url.replace(self.addr,".")))
        self.get('LabelTestPhoto')['image'] = self.test_img

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

