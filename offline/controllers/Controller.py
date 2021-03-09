class Controller(object):
    def __init__(self, models):
        self.half_time = models["AllHalfTime"]
        self.all_highlights = models["AllHighlights"]
        self.match = models["Match"]
        self.videos = models["Videos"]