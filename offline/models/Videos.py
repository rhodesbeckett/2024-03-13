import os
import random

class Videos(object):
    videos_src = ""
    ok = False
    cutted = False

    def set_src(self, video):
        if video == "":
            video = "video{}".format(str(random.randint(1,1000)))
        self.videos_src = video

    def create_video_location(self):
        if self.videos_src != "":
            if self.videos_src not in os.listdir("."):
                os.mkdir(self.videos_src)
        else:
            print("Program is not ready for cutting.")

    def is_duplicate(self, sufix):
        for i in os.listdir(self.videos_src):
            if i.endswith(sufix):
                return True
        return False

    def list_of_videos(self):
        return os.listdir(self.videos_src)

    def name_start(self, prefix):
        for i in self.list_of_videos():
            if i.startswith(prefix):
                return i

    def add_to_txt_file(self,name):
        with open(self.videos_src + "/" + "mylist.txt","a") as txt_file:
            line = "file '{}'\n".format(name)
            txt_file.write(str(line))