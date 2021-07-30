from controller.Video import Video
import os
import subprocess


class Merging(Video):
    def __init__(self, ID):
        self.set_id(ID)

    def merge_videos(self):
        if self.can_merge():
            self.make_merge_txt_file()
            self.merge()

    def can_merge(self):
        self.create_video_location()
        if "firstHalf.mp4" and "secondHalf.mp4" in os.listdir(self.highlights_location):
            return True
        else:
            return False

    def make_merge_txt_file(self):
        with open(f'{self.highlights_location}/final.txt', "w") as txt_file:
            txt_file.writelines("file 'firstHalf.mp4'\n")
            txt_file.writelines("file 'secondHalf.mp4'\n")

    def merge(self):
        txt_file = f'{self.highlights_location}/final.txt'
        output_name = f'{self.highlights_location}/final.mp4'
        if os.path.exists(output_name):
            os.unlink(output_name)
        command = f'ffmpeg -f concat -safe 0 -i "{txt_file}" -c copy "{output_name}"'
        subprocess.call(command, shell=True)
