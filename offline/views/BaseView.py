from easy_tk import EasyTkObject


class BaseView(EasyTkObject):
    frame_path = ""

    def __init__(self,controller):
        super(BaseView,self).__init__()
        self.controller = controller
    
    def adding_complete_widgets(self,root,widget):
        self.easy.add_complete_widget(root)
        self.easy.add_complete_widget(widget)

    def widget_decorator(func):
        def wrapper(*args,):
            args[0].method_part()
            func(args[0])
            args[0].frame_part()
        return wrapper

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

""" class BaseViewDecorator(object):
     """