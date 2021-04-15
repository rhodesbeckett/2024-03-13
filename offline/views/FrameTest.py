from views.BaseView import BaseView

class FrameTest(BaseView):
    
    def __init__(self):
        super(FrameTest,self).__init__()
        self.frame_path = "views/json/testing.json"
        self.json_frame = "FrameTest"
        self.tab_text = "Testing"