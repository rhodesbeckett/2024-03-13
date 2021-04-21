from tkinter import Entry,StringVar

class TimeInput(Entry):
    counter = 0

    def __init__(self, master=None, cnf={}, **kw):
        super(TimeInput,self).__init__(master,cnf={},**kw)
        self['textvariable'] = self.set_listener()
        TimeInput.counter += 1
        self.set_length()

    def unos(self,sv):
        value = sv.get()
        if len(value) < self.value_length + 1:
            if not value.isnumeric():
                sv.set(self.fix_input(value,len(value)))
        else:
            sv.set(self.fix_input(value,self.value_length))
    
    def fix_input(self,input,end):
        return input[0:end]

    def set_listener(self):
        sv = StringVar()
        sv.trace('w',lambda name, index, mode, sv=sv: self.unos(sv))
        return sv

    def set_length(self):
        if TimeInput.counter == 1:
            self.value_length = 3
        elif TimeInput.counter == 2:
            self.value_length = 2
        elif TimeInput.counter == 3:
            self.value_length = 2
            TimeInput.counter = 0

        