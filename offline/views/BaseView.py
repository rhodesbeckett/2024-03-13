from easy_tk import EasyTkObject


class BaseView(EasyTkObject):
    frame_path = ""
    
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
    
    
    @widget_decorator
    def create_widgets(self):
        self.open_file(self.frame_path)
        self.reading_from_json()

""" class BaseViewDecorator(object):
     """