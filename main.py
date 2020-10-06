from GUIs.Root import *

root = Root()
try:
	root.bind("<Tab>",root.keypress)
	root.bind("g",root.keypress)
	root.bind("G",root.keypress)
	root.bind("f",root.keypress)
	root.bind("F",root.keypress)
	root.bind('<Control-Key-s>', root.keypress)
	root.bind('<Control-Key-S>', root.keypress)
	root.grid()
	root.geometry("1001x285")
	root.mainloop()
except:
	print("")



# from tkinter import *
#
# from utils.tkw.TKWIdgets import TKWidgets
#
# root = Tk()
# tkw = TKWidgets(root)
#
# tkw.insert(Label, 0, tkw.setData("aa"))
# tkw.insert(Label, 0, tkw.setData("aa2"))
# tkw.insert(Label, 0, tkw.setData("aa3"))
# tkw.insert(Button, 0, tkw.setData("aa4aaaaa", row=1, column=0, columnspan=3))
# # tkw.addNewRow(0)
# root.grid()
# root.mainloop()