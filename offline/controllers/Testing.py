import os
from PIL import Image,ImageTk
import cv2
from controllers.Controller import Controller

class Testing(Controller):
    # u konstruktoru ima sve modele,svaki controllers ima sve
    half_time_tested = False
    counter = 0

    def test_match(self, window):
        if self.match.validate_location():
            self.counter+=1
            window.get("LabelMessageMatch")["bg"] = "green"
        else:
            window.get("LabelMessageMatch")["bg"] = "red"

    def test_half_time(self, window):
        seconds = self.half_time.get_seconds()
        if seconds > 0:
            if seconds < self.match.get_match_seconds():
                self.counter+=1
                window.get(self.half_time.test_label)["bg"] = "green"
                return None
            window.get(self.half_time.test_label)["bg"] = "red"
        elif seconds == 0:
            window.get(self.half_time.test_label)["bg"] = "red"
            return None

    def test_highlights(self, window):
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
                window.get("LabelHighlightsMessage")["bg"] = "green"
                self.all_highlights.seconds = temp_list[:]
                self.counter += 1
        else:
            window.get("LabelHighlightsMessage")["bg"] = "red"

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
            self.test_img = ImageTk.PhotoImage(slika)
            easy.get("LabelTestPhoto")["image"] = self.test_img

        def get_seconds():
            return self.half_time.get_seconds()

        can_run = [self.match.can_take_photo,]
        if False not in can_run:
            min = int(easy.get("EntryTimeStampMin").get())
            sec = int(easy.get("EntryTimeStampSec").get())
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
            row.row[0]["bg"] = "#f0f0f0"
            row.row[1]["bg"] = "#f0f0f0"
            row.row[2]["bg"] = "#f0f0f0"
        return start, end