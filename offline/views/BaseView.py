from easy_tk import EasyTkObject
from views.ViewDecorator import widget_decorator

class BaseView(EasyTkObject):
    frame_path = ""

    def __init__(self,controller):
        super(BaseView,self).__init__()
        self.controller = controller
        self.dimensions = ""
        self.frame_to_raise = ""
    
    def adding_complete_widgets(self,root,widget):
        self.easy.add_complete_widget(root)
        self.easy.add_complete_widget(widget)

    def set_models(self, models):
        self.match = models["Match"]
        self.half_time = models["AllHalfTime"]
        self.videos = models["Videos"]
        self.all_highlights = models["AllHighlights"]

    def method_part(self):
        pass

    def frame_part(self):
        pass
    
    def set_font(self,widgets):
        for i in self.easy.all_widgets:
            for j in widgets:
                try:
                    if isinstance(self.easy.all_widgets.get(i).get(), j):
                        self.easy.all_widgets.get(i).get()["font"] = ('Minion Pro SmBd', 18, '')
                        break
                except:
                    continue
    
    @widget_decorator
    def create_widgets(self):
        self.open_file(self.frame_path)
        self.reading_from_json()

    def tkraise(self):
        self.get("root").geometry(self.dimensions)
        self.get("root").update()
        self.get(self.frame_to_raise).tkraise()
    """ @raise_decorator
    def tkraise(self,frame,dimensions):
        pass """

""" class BaseViewDecorator(object):
     """