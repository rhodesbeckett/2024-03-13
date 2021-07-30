from controller.Video import Video
from PIL import Image
from cv2 import cv2


class TestingPicture(Video):

    def __init__(self, ID):
        self.set_id(ID)

    def test_photo(self, minute, second):
        self.set_seconds()
        self.set_video_capture()
        row = {"min": minute, "sec": second}
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
