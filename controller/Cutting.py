from controller.Video import Video
import json
import requests
from moviepy.video.io.VideoFileClip import VideoFileClip


class Cutting(Video):
    def __init__(self, ID):
        self.set_id(ID)

    def set_id(self, ID):
        super().set_id(ID)
        self.canCut = json.loads(requests.get(
            f'http://localhost:5000/get/{ID}/cutAndRender.canCut').json()['canCut'])
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
        url = f'http://localhost:5000/update/{self.matchID}/cutAndRender.cutProgress'
        data = {"cutAndRender.cutProgress": progress}
        requests.post(url, data)
