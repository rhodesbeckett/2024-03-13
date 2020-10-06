from tkinter import *
from GUIs.FootballFrame import FootballFrame
from GUIs.HighlightsFrame import HighlightsFrame
from GUIs.TestFrame import TestFrame
from editor.FootballEditor import FootballEditor
from tkinter import messagebox
from utils.Utils import keyPress
from utils.Testing import Testing
import os


class Root(Tk):
	licenca = False


	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)
		container = self.setContainer()
		self.page_name = ""
		self.prozori = {}
		self.footballEditor = FootballEditor()
		self.resizable(False, False)
		self.setAllFrames(container)
		self.prebaci_frejm("FootballFrame")
		self.test = Testing(self)

	# SVE INSTANCE FRAMEOVA
	def setAllFrames(self, container):
		for frejm in (FootballFrame, HighlightsFrame, TestFrame):
			self.page_name = frejm.__name__
			frame = frejm(container, controller=self, fe=self.footballEditor)
			self.prozori[self.page_name] = frame
			frame.grid(row=0, column=0, sticky="nsew")

	# PODESAVANJE KONTEJNERA
	def setContainer(self):
		container = Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		return container

	# PREBACIVANJE NA DRUGE PROZORE
	def prebaci_frejm(self, page_name):
		self.page_name = page_name
		prozor = self.prozori[page_name]
		prozor.tkraise()

		if page_name == "TestFrame":
			self.setScreen("1232x442")
			self.runTest(prozor)
			self.closeIfNeeded()
		elif page_name == "FootballFrame":
			self.setScreen("1001x285")
			self.closeIfNeeded()
		elif page_name == "HighlightsFrame":
			self.setScreen("940x379")
			self.closeIfNeeded()
	# PODESAVANJE VELICINE EKRANA
	def setScreen(self, res):
		self.geometry(res)
		self.update()
	# TASTATURA PRECICE ITD.
	def keypress(self, event):
		keyPress(self, event)

	# PREBACIVANJE NA TEST FRAME
	def runTest(self, prozor):

		# DOBIJANJE POCETKA PRVOG I DRUGOG POLUVREMENA
		prvo = self.prozori["FootballFrame"].get1st()
		drugo = self.prozori["FootballFrame"].get2nd()
		allElements = self.prozori["HighlightsFrame"].getAllElements()
		stringVars = self.prozori["HighlightsFrame"].stringVars
		# PROVERA UTAKMICE
		self.prozori["TestFrame"].setFrame(prozor)
		self.prozori["TestFrame"].checkAll(prvo,drugo,allElements,stringVars)


		# SAKRIVANJE WIDGETA ZA POLUVREME
		if self.footballEditor.tipHighlightsa == "firstRegular":
			prozor.hidePoluvremeWidgets("prvo")
		elif self.footballEditor.tipHighlightsa == "secondRegular":
			prozor.hidePoluvremeWidgets("drugo")
		elif self.footballEditor.tipHighlightsa == "regularFull":
			prozor.hidePoluvremeWidgets("full")

	def proveraLicence(self):
		putanjaFull = str(os.getcwd())
		provera = "footballEditor" not in putanjaFull
		if provera == False:
			self.licenca = False
			return False
		else:
			self.licenca = True
			return True

	def closeIfNeeded(self):
		if self.proveraLicence() == True:
			return None
		else:
			messagebox.showinfo('Error', ' ')
			self.destroy()
			self.quit()

