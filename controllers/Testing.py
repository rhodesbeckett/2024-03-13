import os
from PIL import Image,ImageTk
import cv2

class Testing(object):
    # u konstruktoru ima sve modele,svaki controllers ima sve
    half_time_tested = False
    counter = 0
    def __init__(self, models):
        self.half_time = models["AllHalfTime"]
        self.all_highlights = models["AllHighlights"]
        self.match = models["Match"]
        self.videos = models["Videos"]

    def test_match(self, easy):
        if self.match.validate_location():
            self.counter+=1
            easy.set("text", "OK", 0, 2)
        else:
            easy.set("text", "NOT OK", 0, 2)

    def test_half_time(self, easy_set):
        seconds = self.half_time.get_seconds()
        if seconds > 0:
            if seconds < self.match.get_match_seconds():
                self.counter+=1
                easy_set.set("text", "OK", 0, self.half_time.test_label_index)
                return None
            easy_set.set("text", "NOT OK", 0, self.half_time.test_label_index)
        elif seconds == 0:
            easy_set.set("text", "NOT OK", 0,self.half_time.test_label_index)
            return None

    def test_highlights(self, easy):
        ok = True
        temp_list = []
        for i in self.all_highlights.all.values():
            start, end = self.check_row(i)
            if 0 in (start,end):
                ok = False
            else:
                temp_list.append((start,end))

        if ok == True:
            if self.counter == 2:
                easy.set("text", "OK", 0, 12)
                self.all_highlights.seconds = temp_list[:]
                self.counter += 1
        else:
            easy.set("text", "NOT OK", 0, 12)

    def test_photo(self, easy):
        def make_dir():
            try:
                if not os.path.exists('slike'):
                    os.makedirs('slike')
            except OSError:
                print('Error: Creating directory of data')

            name = './slike/frame' + '.jpg'
            return name

        def save_to_photo(self,easy):
            self.match._cv2.set(1, frejm)
            ret, frame = self.match._cv2.read()
            cv2.imwrite(name, frame)
            self.match._cv2.release()
            cv2.destroyAllWindows()

            slika = Image.open("./slike/frame.jpg")
            slika = slika.resize((651, 305), Image.ANTIALIAS)
            self.testImg = ImageTk.PhotoImage(slika)
            easy.set("image", self.testImg, 0, 10)

        def get_seconds():
            return self.half_time.get_seconds()

        can_run = [self.match.can_take_photo,]
        if False not in can_run:
            min = int(easy.get_text(1, 0))
            sec = int(easy.get_text(1, 2))
            print(sec)
            #
            name = make_dir()
            sec = get_seconds() + min * 60 + sec - self.half_time.to_sub
            frejm = int(self.match.get_fps() * sec)
            #
            if not frejm > self.match.get_sum_frames():
                save_to_photo(self,easy)
                self.tested = True
                self.match.reload_cv2()

    def test_all(self,easy):
        self.counter = 0
        for i in [self.test_match,self.test_half_time,self.test_highlights]:
            previous_counter = self.counter
            i(easy)
            if self.counter <= previous_counter:
                break

    def check_row(self, row):
        half_time = self.half_time.get_seconds(row.half_time)
        start = half_time + row.get_start() - self.half_time.to_sub
        end = start + row.get_end()
        if start >= self.match.get_match_seconds() or start == half_time or row.get_start() == 0:
            row.row[0]["bg"] = "#eb4034"
            row.row[1]["bg"] = "#eb4034"
            start = 0
        if end >= self.match.get_match_seconds() or row.get_end() <= 0:
            row.row[2]["bg"] = "#eb4034"
            end = 0
        if (start and end) not in (0,):
            row.row[0]["bg"] = "SystemWindow"
            row.row[1]["bg"] = "SystemWindow"
            row.row[2]["bg"] = "SystemWindow"
        return start, end