import os
import subprocess
from controllers.Controller import Controller

class Rendering(Controller):
    txt_file_name = ""

    def is_ready(self):
        return self.videos.cutted

    def render(self):
        outputName = self.videos.videos_src + "\\output" + self.match.get_extt()
        if (os.path.exists(outputName)):
            os.unlink(outputName)
        command = f'ffmpeg -f concat -safe 0 -i "{self.videos.videos_src}/mylist.txt" -c copy "{self.videos.videos_src}/output.mp4"'
        subprocess.call(command, shell=True)
        """ os.startfile(self.videos.videos_src) """
        return 0