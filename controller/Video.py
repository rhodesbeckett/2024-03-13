import os
import mimetypes
from cv2 import cv2
import requests
import json
import time


class Video():

    def __init__(self):
        self.mc = {}
        self._cv2 = {}
        self.seconds = 0

    def set_id(self, ID):
        self.mc = json.loads(requests.get(
            f'http://localhost:5000/get/{ID}/compDesc').json()['compDesc'])
        self.highlights = json.loads(requests.get(
            f'http://localhost:5000/get/{ID}/highlights').json()['highlights'])
        self.matchID = ID

    def validate_location(self, src):
        if os.path.exists(src):
            if os.path.isfile(src):
                if mimetypes.guess_type(src)[0].startswith('video'):
                    return True
            return False
        return False

    def create_video_location(self):
        self.highlights_location = f'highlights/{self.mc["title"]}'
        if self.mc['title'] not in os.listdir("highlights"):
            os.mkdir(self.highlights_location)

    def get_match_seconds(self):
        frame_per_second = self.get_fps()
        ukupno_frejmova = self.get_sum_frames()
        return int(ukupno_frejmova / frame_per_second)

    def get_fps(self):
        frame_per_second = 0.0
        frame_per_second = self._cv2.get(cv2.CAP_PROP_FPS)
        return frame_per_second

    def get_sum_frames(self):
        return int(self._cv2.get(cv2.CAP_PROP_FRAME_COUNT))

    def get_seconds_start(self, row):
        if self.mc['editing'] == "secondHalf":
            return self.seconds + row['min'] * 60 + row['sec'] - 2700
        return self.seconds + row['min'] * 60 + row['sec']

    def get_progress_part(self):
        length = 0
        for row in self.highlights:
            if row['editing'] == self.mc['editing']:
                length += 1
        return 100 / length

    def reset_progress(self, process):
        time.sleep(5)
        if process == 'cut':
            self.update_cut_progress(0.0)

    def update_cut_progress(self, progress):
        pass

    def set_seconds(self):
        editing = self.mc['editing']
        minute = self.mc['time'][editing]['min']
        second = self.mc['time'][editing]['sec']
        self.seconds = minute * 60 + second
