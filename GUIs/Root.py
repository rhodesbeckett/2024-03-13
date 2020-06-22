from tkinter import *
from GUIs.FootballFrame import FootballFrame
from GUIs.HighlightsFrame import HighlightsFrame
from GUIs.TestFrame import TestFrame
from editor.FootballEditor import FootballEditor
from tkinter import messagebox

import os
class Root(Tk):
	licenca = False
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		self.page_name = ""
		self.prozori = {}
		self.footballEditor = FootballEditor()
		# self.resizable(False, False)
		for frejm in (FootballFrame, HighlightsFrame, TestFrame):
			self.page_name = frejm.__name__
			frame = frejm(container, controller=self, fe=self.footballEditor)
			self.prozori[self.page_name] = frame
			frame.grid(row=0, column=0, sticky="nsew")
		self.prebaci_frejm("FootballFrame")


	def prebaci_frejm(self, page_name):
		self.page_name = page_name
		prozor = self.prozori[page_name]
		prozor.tkraise()

		if (page_name == "TestFrame"):
			self.geometry("1232x442")
			self.update()
			self.page_name = page_name
			self.runTest(prozor)
			self.closeIfNeeded()
		elif(page_name=="FootballFrame"):
			self.geometry("1001x285")
			self.update()
			self.closeIfNeeded()
		elif(page_name=="HighlightsFrame"):
			self.geometry("940x379")
			self.update()
			self.closeIfNeeded()

	def keypress(self, event):
		if (event.char == "\t"):
			if(self.page_name == "HighlightsFrame"):
				self.prozori["HighlightsFrame"].clickOnTab()
		elif (event.char == "g" or event.char == "G"):
			self.prebaci_frejm("FootballFrame")
			self.prozori["HighlightsFrame"].removeG(event.char)
		elif (event.char == "f" or event.char == "F"):
			if (self.page_name == "HighlightsFrame"):
				self.prozori["HighlightsFrame"].addRow()
				self.prozori["HighlightsFrame"].removeG(event.char)
		elif (event.char == "e" or event.char == "E"):
			self.prozori["HighlightsFrame"].setTrenutnoVreme("extra")
			self.prozori["HighlightsFrame"].addRow("extra")
			self.prozori["HighlightsFrame"].removeG(event.char)
			if(self.prozori["FootballFrame"].visibleExtraFrame == False):
				self.prozori["FootballFrame"].showOrHideExtraFrame(True)
		elif (event.char == '\x13'):
				self.prozori["HighlightsFrame"].saveToFile()
	def runTest(self,prozor):
		prvo = self.prozori["FootballFrame"].get1st()
		drugo = self.prozori["FootballFrame"].get2nd()

		extraProvera = self.prozori["FootballFrame"].visibleExtraFrame
		prvoExtra = self.prozori["FootballFrame"].get1stExtra()
		drugoExtra = self.prozori["FootballFrame"].get2ndExtra()

		stringVars = self.prozori["HighlightsFrame"].stringVars
		prozor.checkMatch()
		prozor.checkPoluvreme(prvo, drugo)
		prozor.checkExtra(extraProvera,prvoExtra,drugoExtra)
		prozor.checkHighlights(self.prozori["HighlightsFrame"].getAllElements(), stringVars)

	def proveraLicence(self):
		putanjaFull = str(os.getcwd())
		provera = "projekat2-nrs" in putanjaFull
		if (provera==False):
			self.licenca = False
			return False
		else:
			self.licenca = True
			return True
	def closeIfNeeded(self):
		if(self.proveraLicence()==True):
			return None
		else:
			messagebox.showinfo('Error', ' ')
			self.destroy()
			self.quit()


