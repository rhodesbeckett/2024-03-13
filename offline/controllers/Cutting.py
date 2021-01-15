from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


class Cutting(object):

    def __init__(self, models):
        self.half_time = models["AllHalfTime"]
        self.all_highlights = models["AllHighlights"]
        self.match = models["Match"]
        self.videos = models["Videos"]

    def check_start(self):
        return 0

    def check_end(self):
        return 0

    def cut_all(self):
        self.videos.create_video_location()
        counter = 0
        for i in self.all_highlights.seconds:
            self.cut_one(i[0], i[1], counter)
            counter += 1
        self.videos.cutted = True

    def cut_one(self, start, end, counter):
        second_part = "_" + str(start) + str(end) + self.match.get_extt()
        name = self.videos.videos_src + "/video" + str(counter) + second_part
        if self.videos.is_duplicate(second_part) == False:
            fajl = VideoFileClip(self.match.get_src())
            new = fajl.subclip(start, end)
            if (self.match.get_extt() == ".mp4"):
                new.write_videofile(name, logger=None)
            else:
                ffmpeg_extract_subclip(self.match.get_src(), start, end, targetname=name)

    def file_exist(self):
        return 0
