from views.BaseView import BaseView

class FrameHome(BaseView):
    def __init__(self):
        super(FrameHome,self).__init__()
        self.frame_path = "views/json/home.json"
        self.json_frame = "FrameHome"
        self.tab_text = "Home"
    
    def frame_part(self):
        self.add_comp()

    def add_comp(self):
        self.open_file("views/json/compCard.json")
        self.reading_from_json()
        
    