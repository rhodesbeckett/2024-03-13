from controller.Video import Video
import json
import requests
from moviepy.video.io.VideoFileClip import VideoFileClip
from bson.objectid import ObjectId


class Cutting(Video):
    def __init__(self, collection, ID):
        self.collection = collection
        self.set_id(ID)

    def set_id(self, ID):
        super().set_id(ID)
        self.canCut = self.collection.find_one({"_id": ObjectId(ID)})[
            'cutAndRender']['canCut']
        self.highlights_location = f'highlights/{self.mc["title"]}'

    def cut_all(self):
        self.set_seconds()
        if self.canCut is True:
            self.progress_part = self.get_progress_part()
            with open(f'{self.highlights_location}/mylist.txt', 'w') as txt_file:
                for row in self.highlights:
                    if row['editing'] == self.mc['editing']:
                        self.cut_one(row)
                        file_name = f'\'video{self.video_id}\''
                        txt_file.write(f'file {file_name}\n')
                self.reset_progress('cut')

    def cut_one(self, row):
        start = self.get_seconds_start(row)
        end = start + row['toAdd']
        self.video_id = f'_{start}{end}.mp4'
        name = f'{self.highlights_location}/video{self.video_id}'
        fajl = VideoFileClip(self.mc["src"])
        new = fajl.subclip(start, end)
        new.write_videofile(name, logger=None)
        progress = self.progress_part * (self.highlights.index(row) + 1)
        self.update_cut_progress(progress)

    def update_cut_progress(self, progress):
        data = {"cutAndRender.cutProgress": progress}
        self.collection.update_one(
            {"_id": ObjectId(self.matchID)}, {"$set": data})
