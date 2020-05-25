from tkinter import *
from GUIs.FootballFrame import FootballFrame
from GUIs.HighlightsFrame import HighlightsFrame
from GUIs.TestFrame import TestFrame
from editor.FootballEditor import FootballEditor


class Root(Tk):
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.prozori = {}
		self.footballEditor = FootballEditor()

		for frejm in (FootballFrame, HighlightsFrame, TestFrame):
			page_name = frejm.__name__
			frame = frejm(container, controller=self, fe=self.footballEditor)
			self.prozori[page_name] = frame
			frame.grid(row=0, column=0, sticky="nsew")
		self.prebaci_frejm("FootballFrame")

	def prebaci_frejm(self, page_name):
		prozor = self.prozori[page_name]
		prozor.tkraise()

		if (page_name == "TestFrame"):
			self.runTest(prozor)
		elif(page_name=="FootballFrame"):
			self.geometry("589x189")
			self.update()
		elif(page_name=="HighlightsFrame"):
			self.geometry("940x379")
			self.update()

	def keypress(self, event):
		if (event.char == "\t"):
			self.prozori["HighlightsFrame"].clickOnTab()
		elif (event.char == "g" or event.char == "G"):
			self.prebaci_frejm("FootballFrame")
			self.prozori["HighlightsFrame"].removeG(event.char)
		elif (event.char == "f" or event.char == "F"):
			self.prozori["HighlightsFrame"].addRow()
			self.prozori["HighlightsFrame"].removeG(event.char)
	def runTest(self,prozor):
		prvo = self.prozori["FootballFrame"].get1st()
		drugo = self.prozori["FootballFrame"].get2nd()
		stringVars = self.prozori["HighlightsFrame"].stringVars
		prozor.checkMatch()
		prozor.checkPoluvreme(prvo, drugo)
		prozor.checkHighlights(self.prozori["HighlightsFrame"].getAllElements(), stringVars)
		self.geometry("1232x442")
		self.update()
