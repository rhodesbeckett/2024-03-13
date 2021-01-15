import datetime

class HighlightsRow(object):
    def __init__(self):
        self.row = []

    def add_entry(self,entry):
        self.row.append(entry)

    def is_entry_digit(self, index):
        if self.get_text(index).isdigit():
            return True
        return None

    def check_entries(self):
        yes = []
        no = []
        for i in range(len(self.row)):
            if self.is_entry_digit(i):
                yes.append(self.row[i])
            else:
                no.append(self.row[i])
        return yes,no

    def get_start(self):
        try:
            min = self.get_text(0)
            sec = self.get_text(1)
            return int(datetime.timedelta( minutes=int(min) , seconds = int(sec) ).total_seconds())
        except:
            return 0

    def get_end(self):
        try:
            return int(self.get_text(2))
        except:
            return 0

    def get_text(self,index):
        return self.row[index].get()
