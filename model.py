import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import os
import mimetypes
from cv2 import cv2
import requests
import json
from moviepy.video.io.VideoFileClip import VideoFileClip
import time
import os
import subprocess
from PIL import Image,ImageTk

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["videosdb"]
collection = mydb["matchCompilations"]


class Model():
    def __init__(self):
        pass

    def insert(self):
        matchComp = {
            "compDesc": {
                "title": "",
                "src": "",
                "editing": "",
                "time": {
                    "isChosen": False,
                    "firstHalf": {"min": None, "sec": None},
                    "secondHalf": {"min": None, "sec": None}
                }
            },
            "highlights": [],
            "testing": {
                "src": False,
                "halfTime": False,
                "highlights": False
            },
            "cutAndRender": {
                "canCut": False,
                "canRender": False,
                "cutProgress": 0,
                "renderProgress": 0
            }
        }
        return collection.insert_one(matchComp)

    def get(self, ID, key):
        comp = collection.find_one({"_id": ObjectId(ID)})
        return get_data(comp, key)

    def get_all(self):
        comps = collection.find({})
        return {"allComps":dumps(comps)}

    def delete_all(self):
        collection.delete_many({})

    def update(self, request, ID, key):
        new_property = {"$set": {key: get_property(request, ID, key)}}
        collection.update_one({"_id": ObjectId(ID)}, new_property)

    def test(self,ID):
        testing = Testing(ID) 
        testing.test_all()
        return testing.test_response

    def cut(self,ID):
        cutting = Cutting(ID)
        cutting.cut_all()
    
    def render(self,ID):
        rendering = Rendering(ID)
        rendering.render()
    
    def merge_videos(self,ID):
        merging = Merging(ID)
        merging.merge_videos()
    
    def get_photo(self,ID,minute,second):
        return TestingPicture(ID).test_photo(minute,second)

# helper functions
def get_data(comp: object, key: str):
    keys = key
    result = {}
    if "." in key:
        keys = key.split(".")
        document = keys[0]
        key_object = keys[1]
        result[key_object] = dumps(comp[document][key_object])
    else:
        result[key] = dumps(comp[key])
    return result


def get_property(request, ID, key):
    if key == "cutAndRender.canCut" or key == "cutAndRender.canRender":
        try:
            response = request.get_json(force=True)
            return response
        except:
            return False
    elif key == "cutAndRender.cutProgress" or key == "cutAndRender.renderProgress":
        """ .split("cutProgress=")[1] """
        return float(request.get_data(key).decode("UTF-8").split(f'{key}=')[1])
    else:
        return request.get_json(force=True)



class Video():
    
    def __init__(self):
        self.mc = {}
        self._cv2 = {}
        self.seconds = 0
    
    def set_id(self,ID):
        self.mc = json.loads(requests.get(f'http://localhost:5000/get/{ID}/compDesc').json()['compDesc'])
        self.highlights = json.loads(requests.get(f'http://localhost:5000/get/{ID}/highlights').json()['highlights'])
        self.matchID = ID
      
    def validate_location(self,src):
        if os.path.exists(src):
            if os.path.isfile(src):
                if mimetypes.guess_type(src)[0].startswith('video'):
                    return True
            return False
        return False

    def create_video_location(self):
        self.highlights_location = f'highlights/{self.mc["title"]}'
        if self.mc['title'] not in os.listdir("highlights"):
            os.mkdir(self.highlights_location)


    def get_match_seconds(self):
        frame_per_second = self.get_fps()
        ukupno_frejmova = self.get_sum_frames()
        return int(ukupno_frejmova / frame_per_second)
        
    def get_fps(self):
        frame_per_second = 0.0
        frame_per_second = self._cv2.get(cv2.CAP_PROP_FPS)
        return frame_per_second

    def get_sum_frames(self):
        return int(self._cv2.get(cv2.CAP_PROP_FRAME_COUNT))


    def get_seconds_start(self,row):
        if self.mc['editing'] == "secondHalf":
            return self.seconds + row['min'] * 60 + row['sec'] -2700
        return self.seconds + row['min'] * 60 + row['sec']

    def get_progress_part(self):
        length = 0
        for row in self.highlights:
            if row['editing'] == self.mc['editing']:
                length += 1
        return 100 / length

    def reset_progress(self,process):
        time.sleep(5)
        if process == 'cut':
            self.update_cut_progress(0.0)
    
    def update_cut_progress(self,progress):
        pass

    def set_seconds(self):
        editing = self.mc['editing']
        minute = self.mc['time'][editing]['min']
        second = self.mc['time'][editing]['sec']
        self.seconds = minute * 60 + second

class Testing(Video):

    def __init__(self, ID):
        self.set_id(ID)
        self.counter = 0
        self.test_response = {}

    def test_all(self):
        self.counter = 0
        self.test_response = {'src': False,
                              'halftime': False, 'highlights': False}
        for i in [self.check_match, self.check_halftime, self.check_highlights]:
            previous_counter = 0
            i()
            if self.counter <= previous_counter:
                break
        self.update_testing()

    def check_match(self):
        title = self.mc["title"]
        src = self.mc["src"]
        if title != "" and self.validate_location(src):
            self.create_video_location()
            self.test_response['src'] = True
            self._cv2 = cv2.VideoCapture(src)
            self.counter += 1
        else:
            self.test_response['src'] = False

    def check_halftime(self):
        editing = self.mc['editing']
        if self.mc['time']['isChosen'] == True:
            minute = self.mc['time'][editing]['min'] 
            second = self.mc['time'][editing]['sec'] 
            self.seconds = minute * 60 + second
            if self.seconds > 0 and self.seconds < self.get_match_seconds():
                self.counter += 1
                self.test_response['halftime'] = True 
            else:
                self.test_response['halftime'] = False

    def check_highlights(self):
        for row in self.highlights:
            if self.row_check(row) == True:
                continue
            else:
                return False
        self.test_response['highlights'] = True
        return True

    def row_check(self,row):
        if False in [row['min'] != None,row['sec'] != None,row['toAdd'] != None]:
            return False
        else:
            secondsRow = self.get_seconds_start(row) + row['toAdd']
            if secondsRow < self.get_match_seconds():
                return True
        return False

    def update_testing(self):
        url = f'http://localhost:5000/update/{self.matchID}/testing'
        requests.post(url,json.dumps(self.test_response))

class TestingPicture(Video):

    def __init__(self,ID):
        self.set_id(ID)

    def test_photo(self,minute,second):
        self.set_seconds()
        self.set_video_capture()
        row = {"min":minute,"sec":second}
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

    def set_video_capture(self):
        self._cv2 = cv2.VideoCapture(self.mc['src'])
    
    

class Cutting(Video):
    def __init__(self,ID):
        self.set_id(ID)

    def set_id(self,ID):
        super().set_id(ID)
        self.canCut = json.loads(requests.get(f'http://localhost:5000/get/{ID}/cutAndRender.canCut').json()['canCut'])
        self.highlights_location = f'highlights/{self.mc["title"]}'

    def cut_all(self):
        self.set_seconds()
        if self.canCut == True:
            self.progress_part = self.get_progress_part()
            with open(f'{self.highlights_location}/mylist.txt','w') as txt_file:
                for row in self.highlights:
                    if row['editing'] == self.mc['editing']:
                        self.cut_one(row)
                        file_name = f'\'video{self.video_id}\''
                        txt_file.write(f'file {file_name}\n')
                self.reset_progress('cut')


    def cut_one(self,row):
        start = self.get_seconds_start(row)
        end = start + row['toAdd']
        self.video_id = f'_{start}{end}.mp4'
        name = f'{self.highlights_location}/video{self.video_id}'
        fajl = VideoFileClip(self.mc["src"])
        new = fajl.subclip(start,end)
        new.write_videofile(name,logger= None)
        progress = self.progress_part * (self.highlights.index(row)+1)
        self.update_cut_progress(progress) 
        
    def update_cut_progress(self,progress):
        url = f'http://localhost:5000/update/{self.matchID}/cutAndRender.cutProgress'
        data = {"cutAndRender.cutProgress":progress}
        requests.post(url,data)



class Rendering(Video):
    def __init__(self,ID):
        self.set_id(ID)
    
    def update_render_progress(self,progress):
        url = f'http://localhost:5000/update/{self.matchID}/cutAndRender.renderProgress'
        data = { "cutAndRender.renderProgress": progress }
        requests.post(url,data)

    def render(self):
        self.create_video_location()
        self.progress_part = self.get_progress_part()
        output_name = f'{self.highlights_location}/{self.mc["editing"]}.mp4'
        txt_file_name = f'{self.highlights_location}/mylist.txt'
        if os.path.exists(output_name):
            os.unlink(output_name)
        command = f'ffmpeg -f concat -safe 0 -i "{txt_file_name}" -c copy "{output_name}"'
        subprocess.call(command,shell= True)
        self.update_render_progress(100.0)
        
        self.reset_progress("render")


class Merging(Video):
    def __init__(self,ID):
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
         with open(f'{self.highlights_location}/final.txt',"w") as txt_file:
            txt_file.writelines("file 'firstHalf.mp4'\n")
            txt_file.writelines("file 'secondHalf.mp4'\n") 

    def merge(self):
        txt_file = f'{self.highlights_location}/final.txt'
        output_name = f'{self.highlights_location}/final.mp4'
        if os.path.exists(output_name):
            os.unlink(output_name)
        command = f'ffmpeg -f concat -safe 0 -i "{txt_file}" -c copy "{output_name}"'
        subprocess.call(command,shell= True)
