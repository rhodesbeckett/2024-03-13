from GUIs.Root import *

root = Root()
try:
	root.bind("<Tab>",root.keypress)
	root.bind("g",root.keypress)
	root.bind("G",root.keypress)
	root.bind("f",root.keypress)
	root.bind("F",root.keypress)
	root.bind("e", root.keypress)
	root.bind("E", root.keypress)
	root.bind('<Control-Key-s>', root.keypress)
	root.bind('<Control-Key-S>', root.keypress)
	root.grid()
	root.geometry("1001x285")
	root.mainloop()
except:
	print("")

