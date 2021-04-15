from views.BaseView import BaseView

class FrameMatchInfo(BaseView):

    def __init__(self):
        super(FrameMatchInfo,self).__init__()
        self.frame_path = "views/json/matchInfo.json"
        self.json_frame = "FrameMatchInfo"
        self.tab_text = "MatchInfo"