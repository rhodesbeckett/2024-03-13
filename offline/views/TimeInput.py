from tkinter import Entry,StringVar

class TimeInput(Entry):

    def __init__(self, master=None, cnf={}, **kw):
        super(TimeInput,self).__init__(master,cnf={},**kw)
        self['textvariable'] = self.set_listener()
        self.row = {}
        self.part = "min"

    def unos(self,sv):
        value = sv.get()
        if len(value) < self['width']+1:
            if not value.isnumeric():
                self.row[self.part] = self.fix_input(value,len(value)-1)
                sv.set(self.fix_input(value,len(value)-1))
        else:
            sv.set(self.fix_input(value,self['width']))
            self.row[self.part] = self.fix_input(value,self['width'])
        self.row[self.part] = self.fix_row_input(sv)

    def fix_row_input(self,sv):
        if sv.get() == "":
            return None
        else:
            return int(sv.get())

    def fix_input(self,input,end):
        return input[0:end]

    def set_listener(self):
        self.sv = StringVar()
        self.sv.trace('w',lambda name, index, mode, sv=self.sv: self.unos(sv))
        return self.sv

    def set_model(self,row={},part="min"):
        self.row = row
        self.part = part

    def insert(self, index, string):
        if string == None:
            string = ""
            self.row[self.part] = string
        super().insert(index,string)
        
    def get(self):
        if self.sv.get().isnumeric():
            return int(self.sv.get())
        elif self.sv.get() == "":
            return None