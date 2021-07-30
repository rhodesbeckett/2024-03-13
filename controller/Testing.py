from controller.Video import Video
from cv2 import cv2
from bson.objectid import ObjectId


class Testing(Video):

    def __init__(self, collection, ID):
        self.set_id(ID)
        self.collection = collection
        self.counter = 0
        self.test_response = {}

    def test_all(self):
        self.counter = 0
        self.test_response = {'src': False,
                              'halftime': False, 'highlights': False}
        for i in [self.check_match, self.check_halftime, self.check_highlights]:
            previous_counter = self.counter
            i()
            if self.counter <= previous_counter:
                break
        self.update_testing()

    def check_match(self):
        title = self.mc["title"]
        src = self.mc["src"]
        if title != "" and self.validate_location(src):
            self.create_video_location()
            self.test_response['src'] = True
            self._cv2 = cv2.VideoCapture(src)
            self.counter += 1
        else:
            self.test_response['src'] = False

    def check_halftime(self):
        editing = self.mc['editing']
        if self.mc['time']['isChosen'] is True:
            minute = self.mc['time'][editing]['min']
            second = self.mc['time'][editing]['sec']
            self.seconds = minute * 60 + second
            if self.seconds > 0 and self.seconds < self.get_match_seconds():
                self.counter += 1
                self.test_response['halftime'] = True
            else:
                self.test_response['halftime'] = False

    def check_highlights(self):
        for row in self.highlights:
            if self.row_check(row) is True:
                continue
            else:
                return False
        if len(self.highlights) == 0:
            self.test_response['highlights'] = False
            return None
        self.test_response['highlights'] = True
        return True

    def row_check(self, row):
        if False in [row['min'] != None, row['sec'] != None, row['toAdd'] != None]:
            return False
        else:
            secondsRow = self.get_seconds_start(row) + row['toAdd']
            if secondsRow < self.get_match_seconds():
                return True
        return False

    def update_testing(self):
        new_property = {"$set": {"testing": self.test_response}}
        self.collection.update_one({"_id": ObjectId(self.matchID)}, new_property)
