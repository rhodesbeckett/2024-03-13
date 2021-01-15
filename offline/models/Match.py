import os
import cv2


class Match(object):
    __src = ""
    match_seconds = 0
    match_fps = 0
    _cv2 = object
    can_take_photo = False

    def validate_location(self):
        if os.path.isfile(self.__src):
            if self._cv2 == object:
                self.can_take_photo = True
                self._cv2 = cv2.VideoCapture(self.__src)
            return True
        return False

    def set_match(self, match):
        self.__src = match

    def get_src(self):
        return self.__src

    def get_fps(self):
        frame_per_second = 0.0
        try:
            frame_per_second = self._cv2.get(cv2.CAP_PROP_FPS)
        except RuntimeWarning:
            print("error in checking fps")
        return frame_per_second

    def get_match_seconds(self):
        frame_per_second = self.get_fps()
        ukupno_frejmova = self.get_sum_frames()
        return int(ukupno_frejmova / frame_per_second)

    def get_sum_frames(self):
        return int(self._cv2.get(cv2.CAP_PROP_FRAME_COUNT))

    def get_extt(self):
        return os.path.splitext(self.__src)[1]

    def reload_cv2(self):
        self._cv2 = cv2.VideoCapture(self.__src)