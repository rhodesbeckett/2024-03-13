from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from controllers.Controller import Controller

class Cutting(Controller):


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
                self.videos.add_to_txt_file("video" + str(counter) + second_part)
                new.write_videofile(name, logger=None)
            else:
                self.videos.add_to_txt_file("video" + str(counter) + second_part)
                ffmpeg_extract_subclip(self.match.get_src(), start, end, targetname=name)