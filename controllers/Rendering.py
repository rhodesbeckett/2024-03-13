import os
import subprocess
class Rendering(object):
    txt_file_name = ""

    def __init__(self,models):
        self.half_time = models["AllHalfTime"]
        self.all_highlights = models["AllHighlights"]
        self.match = models["Match"]
        self.videos = models["Videos"]


    def is_ready(self):
        return self.videos.cutted


    def make_txt_file(self):
        self.txt_file_name = self.videos.videos_src + "/" + "mylist.txt"
        imetxtFajl = str(self.txt_file_name)
        txtFajl = open(imetxtFajl, "w")
        for i in range(len(self.videos.list_of_videos())):
            pocetak = "video" + str(i) + "_"
            imeFajla = self.videos.name_start(pocetak)
            if (imeFajla != None):
                line = "file '{}'\n".format(imeFajla)
                txtFajl.write(str(line))
        txtFajl.close()

    def render(self):
        outputName = self.videos.videos_src + "\\output" + self.match.get_extt()
        if (os.path.exists(outputName)):
            os.unlink(outputName)
        command = str(
            'ffmpeg -f concat -safe 0 -i "{}" -c copy "{}/{}{}"'.format(self.txt_file_name, self.videos.videos_src, "output", ".mp4"))
        print(command)
        subprocess.call(command, shell=True)
        os.startfile(self.videos.videos_src)
        return 0