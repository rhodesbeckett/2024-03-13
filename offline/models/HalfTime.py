import datetime

class HalfTime(object):

    def __init__(self):
        self.min = ""
        self.sec = ""
        self.to_sub = 0
        self.can_take_photo = False

    def set_time(self,time):
        self.min = time[0]
        self.sec = time[1]

    def validate_min(self):
        if self.min.isdigit():
            return True
        return False

    def validate_sec(self):
        if self.min.isdigit():
            return True
        return False

    def get_seconds(self):
        try:
            sec = datetime.timedelta(minutes=self.to_seconds("min"),seconds=self.to_seconds("sec")).total_seconds()
            self.can_take_photo = True
            return int(sec)
        except:
            self.can_take_photo = False
            return 0

    def to_seconds(self,var):
        if var == "min":
            return int(self.min)
        else:
            return int(self.sec)

    def smaller_than(self,seconds):
        if self.get_seconds() < seconds:
            return True
        return False