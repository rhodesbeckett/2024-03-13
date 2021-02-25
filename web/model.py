import requests
import json
import os
import cv2
import mimetypes
from PIL import Image,ImageTk
from moviepy.video.io.VideoFileClip import VideoFileClip
import subprocess

class Model(object):
    def __init__(self,collection):
        self.collection = collection
        self.testResponse = {'src':False,'halfTime':False,'highlights':False}
        self.path = './matches'
        self.highlights_location = ""

    def check_match(self):
        title = self.mc["title"]
        src = self.mc["src"]
        if title != "" and self.validate_location(src):
            self.create_video_location()
            self.testResponse['src'] = True
            self._cv2 = cv2.VideoCapture(src)
            self.counter += 1
        else:
            self.testResponse['src'] = False

    def validate_location(self,src):
        if os.path.exists(src):
            if os.path.isfile(src):
                if mimetypes.guess_type(src)[0].startswith('video'):
                    return True
            return False
        return False

    def check_half_time(self):
        
        editing = self.mc['editing']
        if self.mc['time']['isChosen'] == True:
            if editing == 'firstHalf' or editing == 'secondHalf':
                minute = self.mc['time'][editing]['min']
                second = self.mc['time'][editing]['sec']
                if str(minute).isdigit() and str(second).isdigit():
                    self.seconds = minute*60+second
                    if self.seconds > 0:
                        if self.seconds < self.get_match_seconds():
                            # plus cv2 provera
                            self.counter += 1
                            self.testResponse['halfTime'] = True
                else:
                    self.testResponse['halfTime'] = False
            else:
                self.testResponse['halfTime'] = False

    def get_match_seconds(self):
        frame_per_second = self.get_fps()
        ukupno_frejmova = self.get_sum_frames()
        return int(ukupno_frejmova / frame_per_second)
    
    def get_fps(self):
        frame_per_second = 0.0
        try:
            frame_per_second = self._cv2.get(cv2.CAP_PROP_FPS)
        except RuntimeWarning:
            print("error in checking fps")
        return frame_per_second

    def get_sum_frames(self):
        return int(self._cv2.get(cv2.CAP_PROP_FRAME_COUNT))

    def check_highlights(self):
        for row in self.highlights:
            if self.row_check(row) == True:
                continue
            else:
                return False
        self.testResponse['highlights'] = True
        return True

    def row_check(self,row):
        if False in [row['min'] != None,row['sec'] != None,row['toAdd'] != None]:
            return False
        else:
            secondsRow = self.get_seconds_start(row) + row['toAdd']
            if secondsRow < self.get_match_seconds():
                return True
        return False

    def get_seconds_start(self,row):
        if self.mc['editing'] == "secondHalf":
            return self.seconds + row['min'] * 60 + row['sec'] -2700
        return self.seconds + row['min'] * 60 + row['sec']

    def test_all(self):
        self.counter = 0
        for i in [self.check_match,self.check_half_time,self.check_highlights]:
            previous_counter = self.counter
            i()
            if self.counter <= previous_counter:
                break
    
    def set_id(self,ID):
        self.mc = json.loads(requests.get(f'http://localhost:5000/getMC/{ID}').json()['compDesc'])
        self.highlights = json.loads(requests.get(f'http://localhost:5000/getHighlights/{ID}').json()['highlights'])


    def test_photo(self,row):
        seconds = self.get_seconds_start(row)
        frame = int(self.get_fps() * seconds)
        if not frame > self.get_sum_frames():
            self._cv2.set(1, frame)
            ret, frame2 = self._cv2.read()
            cv2.imwrite(f'./static/frame{seconds}.jpg', frame2)
            self._cv2.release()
            cv2.destroyAllWindows()

            slika = Image.open(f'./static/frame{seconds}.jpg')
            slika = slika.resize((651, 305), Image.ANTIALIAS)
            slika.save(f'./static/frame{seconds}.jpg')
            return f'frame{seconds}.jpg'

    def cut_all(self):
        self.test_all()
        for row in self.highlights:
            self.cut_one(row)

    def cut_one(self,row):
        start = self.get_seconds_start(row)
        end = start + row['toAdd']
        video_id = f'_{start}{end}.mp4'
        name = f'{self.highlights_location}/video{video_id}'
        fajl = VideoFileClip(self.mc["src"])
        new = fajl.subclip(start,end)
        new.write_videofile(name,logger= None)

    def create_video_location(self):
        self.highlights_location = f'highlights/{self.mc["title"]}'
        if self.mc['title'] not in os.listdir("highlights"):
            os.mkdir(self.highlights_location)
    

    def sorting_dir(self):
        def sorting_by(x):
            return (x[5:])
        videos = os.listdir(self.highlights_location)
        sorted_videos = sorted(videos, key = sorting_by)
        sorted_videos.remove("mylist.txt")
        return sorted_videos
    
    def make_txt_file(self):
        self.txt_file_name = f'{self.highlights_location}/mylist.txt'
        txt_file = open( self.txt_file_name,"w")
        videos = self.sorting_dir()
        for i in videos:
            line = f'file \'{i}\'\n'
            txt_file.write(line)
        txt_file.close()
    
    def render(self):
        output_name = f'{self.highlights_location}/output.mp4'
        if (os.path.exists(output_name)):
            os.unlink(output_name)
        command = f'ffmpeg -f concat -safe 0 -i "{self.txt_file_name}" -c copy "{output_name}"'
        subprocess.call(command,shell= True)

    def get_dir_sorted(self):
        pass