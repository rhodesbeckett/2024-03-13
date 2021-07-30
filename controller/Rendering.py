from controller.Video import Video
import requests
import os
import subprocess
from bson.objectid import ObjectId


class Rendering(Video):
    def __init__(self, collection, ID):
        self.collection = collection
        self.set_id(ID)

    def update_render_progress(self, progress):
        data = {"cutAndRender.renderProgress": progress}
        self.collection.update_one({"_id": ObjectId(self.matchID)}, data)

    def render(self):
        self.create_video_location()
        self.progress_part = self.get_progress_part()
        output_name = f'{self.highlights_location}/{self.mc["editing"]}.mp4'
        txt_file_name = f'{self.highlights_location}/mylist.txt'
        if os.path.exists(output_name):
            os.unlink(output_name)
        command = f'ffmpeg -f concat -safe 0 -i "{txt_file_name}" -c copy "{output_name}"'
        subprocess.call(command, shell=True)
        self.update_render_progress(100.0)

        self.reset_progress("render")
