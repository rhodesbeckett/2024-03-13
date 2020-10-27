from models.HalfTime import HalfTime

class AllHalfTime(object):
    to_sub = 0
    # "Full match": "full_regular",
    choices = {0: "first_regular",
               1: "second_regular"}
    editing_type = ""
    test_label = 0
    setting = 1

    def __init__(self):
        self.first_half = HalfTime()
        self.second_half = HalfTime()

    def set_editing_type(self, type_):
        if type_ == "second_regular":
            self.test_label = "LabelMessageSecondHalf"
            self.to_sub = 2700
        else:
            self.test_label = "LabelMessageFirstHalf"
        self.editing_type = type_

    def get_seconds(self,half_time=0):
        if self.editing_type == "first_regular" or half_time == 1:
            return self.first_half.get_seconds()
        elif self.editing_type == "second_regular" or half_time == 2:
            return self.second_half.get_seconds()

    def set_time(self,time):
        if self.setting == 1:
            self.first_half.set_time(time)
            self.setting+=1
        elif self.setting == 2:
            self.second_half.set_time(time)
            self.setting = 1