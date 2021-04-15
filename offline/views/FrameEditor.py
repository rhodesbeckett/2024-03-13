from views.BaseView import BaseView
from easy_tk import WindowScrollbar

class FrameEditor(BaseView):
    
    def __init__(self):
        super(FrameEditor,self).__init__()
        self.frame_path = "views/json/scrollbar.json"
        self.tab_text = "Editor"
        self.name = "FrameContainer"
        self.window_scrollbar = WindowScrollbar(self)
    
    def method_part(self):
        self.easy.import_methods({"set_scrollbar":self.window_scrollbar.set_scrollbar})

        """ for i in range(2): """
    def frame_part(self):
        
        self.add_row()
        super().frame_part()
        
    
    def add_row(self):
        self.open_file("views/json/highlights.json")
        self.reading_from_json()