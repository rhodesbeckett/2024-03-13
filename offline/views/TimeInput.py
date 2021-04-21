from tkinter import Entry,StringVar

class TimeInput(Entry):

    def __init__(self, master=None, cnf={}, **kw):
        super(TimeInput,self).__init__(master,cnf={},**kw)
        self['textvariable'] = self.set_listener()

    def unos(self,sv):
        value = sv.get()
        if len(value) < self['width']+1:
            if not value.isnumeric():
                sv.set(self.fix_input(value,len(value)-1))
        else:
            sv.set(self.fix_input(value,self['width']))
    
    def fix_input(self,input,end):
        return input[0:end]

    def set_listener(self):
        sv = StringVar()
        sv.trace('w',lambda name, index, mode, sv=sv: self.unos(sv))
        return sv