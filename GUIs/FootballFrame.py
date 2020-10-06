import os
import threading
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from utils.Renderovanje import *
from utils.Seckanje import *
from utils.Utils import *
from utils.tkw.TKWIdgets import TKWidgets


class FootballFrame(Frame):
	def __init__(self, parent, controller, fe):
		Frame.__init__(self, parent)
		self.footballEditor = fe
		self.controller = controller
		self.grid(row=0, column=0, sticky=W)
		self.tkw = TKWidgets(self)

		self.create_widgets()
		self.fajlDialog = filedialog

	def create_widgets(self):
		self.addFirstTwoButtons()
		self.addRegularTimeFrame()
		self.addOtherWidgets()
		self.showOrHideFrameForCut(False)
		setWidgets(getStyles(self, W, E))

	def addFirstTwoButtons(self):
		# 0 0
		data = self.tkw.setData("MEC", 15, 5, W)
		self.tkw.insert(Button, 0, data)
		self.tkw.set("command", self.btnMethods("mecBtn"))

		# 0 1
		data = self.tkw.setData("HIGHLIGHTS", 15, 5, W)
		self.tkw.insert(Button, 0, data)
		self.tkw.set("command", self.btnMethods("highlightsBtn"))

	def addRegularTimeFrame(self):
		# 0 3
		data = self.tkw.setData("",sticky=E)
		self.tkw.insert(Frame, 0, data, True)

		# 1 0
		data = self.tkw.setData("PRVO POLUVREME",pady=5, sticky=E)
		self.tkw.insert(Label, 1, data)

		# 1 1
		data = self.tkw.setData(" ", (5, 2), 5, E)
		self.tkw.insert(Entry, 1, data)
		self.tkw.set("width", 2)
		# self.tkw.getObject(1,1).insert(0,"2")

		# 1 2
		data = self.tkw.setData(":", (0, 0), 5, E)
		self.tkw.insert(Label, 1, data)

		# 1 3
		data = self.tkw.setData(" ", (5, 2), 5, E)
		self.tkw.insert(Entry, 1, data)
		self.tkw.set("width", 2)
		# self.tkw.getObject(1, 3).insert(0, "57")

		# 1 4
		data = self.tkw.setData("DRUGO POLUVREME", (0, 0), 5, E)
		self.tkw.insert(Label, 1, data)

		# 1 5
		data = self.tkw.setData(" ", (5, 2), 5, E)
		self.tkw.insert(Entry, 1, data)
		self.tkw.set("width", 2)

		# 1 6
		data = self.tkw.setData(":", pady=5, sticky=E)
		self.tkw.insert(Label, 1, data)

		# 1 7
		data = self.tkw.setData(" ", (2, 5), 5, E)
		self.tkw.insert(Entry, 1, data)
		self.tkw.set("width", 2)

	def addOtherWidgets(self):
		self.tkw.add_new_row(0)
		# 0 3
		data = self.tkw.setData("TEST", 15, 5, W)
		self.tkw.insert(Button, 0, data)
		self.tkw.set("command", self.btnMethods("testFrame"))

		# 0 4
		data = self.tkw.setData("RUN", 15, 5, W)
		self.tkw.insert(Button, 0, data)
		self.tkw.set("command", self.btnMethods("rendering"))

		self.footballEditor.tipHighlightsa = "regularFull"

		# 0 5
		data = self.tkw.setData("", sticky= W)
		self.tkw.insert(Frame, 0, data,True)

		# 2 0
		data = self.tkw.setData("JUST CUT", 1, 5, W)
		self.tkw.insert(Button, 2, data)
		self.tkw.set("command", self.btnMethods("cutting"))

		# 2 1
		data = self.tkw.setData("FOLDER", 15, 5, E)
		self.tkw.insert(Label, 2, data)

		# 2 2
		data = self.tkw.setData(" ", 15, 5, E)
		self.tkw.insert(Entry, 2, data)
		self.tkw.set("width", 15)

	def getVideoLocation(self):
		# for i in self.tkw.getParentObject(2).winfo_children():
		# 	print(i)

		lokacija = self.tkw.get_text(2, 2)
		return lokacija

	def showOrHideFrameForCut(self, var):
		if var == True:
			self.tkw.show_children(2, None)
		else:
			self.tkw.hide_children(2, None)

	def get1st(self):
		recnik = {"minut": self.tkw.get_object(1, 1).get(), "sekunda": self.tkw.get_object(1, 3).get()}
		return recnik

	def get2nd(self):
		recnik = {"minut": self.tkw.get_object(1, 5).get(), "sekunda": self.tkw.get_object(1, 7).get()}
		return recnik

	def runRender(self):
		runRender(self, messagebox, os)

	def runCut(self, provera):
		runCut(self, messagebox, provera)

	def getHighlightsType(self):
		return self.footballEditor.tipHighlightsa

	def btnMethods(self, button):
		if button == "mecBtn":
			return lambda var=filedialog, frame=self: self.footballEditor.getPutanja(var, frame)
		elif button == "highlightsBtn":
			return lambda var="HighlightsFrame": self.controller.prebaci_frejm(var)
		elif button == "testFrame":
			return lambda var="TestFrame": self.controller.prebaci_frejm(var)
		elif button == "rendering":
			return lambda var=self: startTRender(var, threading)
		elif button == "cutting":
			return lambda var=self: startTCut(var, threading)
