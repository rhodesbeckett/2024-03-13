import os
# from utils.Utils import convertToSeconds
from utils.Utils import setLabelPoluvreme
class Testing(object):

	def __init__(self,obj):
		self.frame = obj

	def match(self):
		putanja = self.frame.footballEditor.getCurrentPutanja()

		if (os.path.exists(putanja)):
			self.frame.tkw.set("text", "OK", 0, 2)
			self.frame.tkw.get_object(0, 2).bind("<Button-1>", lambda e: self.frame.doNothing())
		else:
			self.frame.tkw.set("text", "NOT OK", 0, 2)
			self.frame.tkw.get_object(0, 2).bind("<Button-1>", lambda e: self.frame.controller.prebaci_frejm("FootballFrame"))

	def poluvremena(self,first, second):
		# prvo
		prvoMinut,prvoSekunda = self.frame.sekundeObj.convertBoth(first)
		setLabelPoluvreme(self.frame, self.frame.tkw.get_object(0, 4), prvoMinut, prvoSekunda, 1)

		drugoMinut,drugoSekunda = self.frame.sekundeObj.convertBoth(second)
		setLabelPoluvreme(self.frame, self.frame.tkw.get_object(0, 6), drugoMinut, drugoSekunda, 2)

	def koloneTest(self,timeStamps):
		what = ["minut","sekunda","sekunda"]
		red = {}
		test = 0
		for i in range(len(timeStamps)):
			timeStamp = timeStamps[i]
			sekunde = self.frame.sekundeObj.convertToSeconds(timeStamp.get(), what[i])
			if (sekunde == None):
				test += 1
				timeStamp["bg"] = "#ff6529"
			else:
				timeStamp["bg"] = "#ffffff"
			if("sekunda" in red):
				red.setdefault("add",sekunde)
			else:
				red.setdefault(what[i],sekunde)

		if(test==0):
			return True,red
		else:
			return False,red

	def brojRedove(self,lista):
		brojac = 0
		for i in lista:

			if(str(type(i)) == "<class 'tkinter.Button'>"):
				brojac+=1
		return brojac-1

	def initVarsForChecking(self):
		vremeUSekundama = []
		self.frame.footballEditor.highlightsCounter = 0
		# time stamp sadrzi entries svaki put po 3
		timeStamp = []
		forAdd = True
		testirano = "ne"
		return vremeUSekundama, timeStamp, forAdd, testirano

