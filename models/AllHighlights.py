from models.HighlightsRow import HighlightsRow
class AllHighlights(object):
    current_row = 0

    half_time = 1
    seconds = []

    def __init__(self):
        self.all = {}


    def create_row(self):
        self.current_row+=1
        self.all.setdefault(self.current_row,self.highlights_factory())

    def add_to_row(self, entry):
        self.all[self.current_row].add_entry(entry)

    def delete_row(self,index):
        row = self.all[index].row
        for i in row:
            i.destroy()
        del self.all[index]

    def highlights_factory(self):
        hr = HighlightsRow()
        hr.half_time = self.half_time
        return hr

    def get_last_row(self):
        try:
            return self.all[self.current_row].row
        except:
            return []



