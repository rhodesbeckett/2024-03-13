from models.HighlightsRow import HighlightsRow
import json


class AllHighlights(object):
    all_indexes = []
    current_row = 0
    half_time = 1
    seconds = []
    widget_json_names = []

    def __init__(self):
        self.all = {}

    def set_names(self,names):
        self.widget_json_names = names

    def create_row(self):
        self.current_row += 1
        self.all.setdefault(self.current_row, self.highlights_factory())
        self.all_indexes.append(self.current_row)

    def add_to_row(self, entry):
        self.all[self.current_row].add_entry(entry)

    def delete_row(self, index):
        row = self.all[index].row
        for i in row:
            i.destroy()
        del self.all[index]
        self.all_indexes.remove(index)

    def highlights_factory(self):
        hr = HighlightsRow()
        hr.half_time = self.half_time
        return hr

    def get_last_row(self):
        try:
            return self.all[self.all_indexes[-1]].row
        except:
            return []

    def get_json_names(self,index):
        names = []
        if index == 1:
            return self.widget_json_names
        for i in self.widget_json_names:
            names.append(i+f'_{index}')
        return names
