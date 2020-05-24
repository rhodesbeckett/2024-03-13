# from editor.FootballEditor import FootballEditor
# fe = FootballEditor()
#
# fe.getPutanja("E:\\Projekat2\\projekat2-nrs\\Liverpool_-_Bournemouth.mkv")
# fe.setPrvoPol("05:09")
# fe.setDrugoPol("59:40")
# fe.provera_fajla("E:\\Projekat2\\projekat2-nrs\\highlights.txt")

from GUIs.Root import *

root = Root()
root.bind("<Tab>",root.keypress)
root.bind("g",root.keypress)
root.bind("G",root.keypress)
root.bind("f",root.keypress)
root.bind("F",root.keypress)

root.grid()
root.geometry("1003x347")
root.mainloop()