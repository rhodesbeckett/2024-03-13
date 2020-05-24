from tkinter import *
from tkinter import filedialog
import os
from editor.FootballEditor import FootballEditor


class FootballFrame(Frame):
	def __init__(self, parent, controller,fe,checker):
		Frame.__init__(self, parent)
		self.footballEditor = fe
		self.checker = checker
		self.controller = controller
		self.grid(row=0, column=0, sticky=W)
		self.create_widgets()
		self.fajlDialog = filedialog

	def create_widgets(self):
		self.mecBtn = Button(self, text="MEC", command=lambda var=filedialog,frame=self: self.footballEditor.getPutanja(var,frame))
		self.mecBtn.grid(row=0, column=0, padx=15, pady=5, sticky=W)

		self.highlightsBtn = Button(self, text="HIGLIGHTS",command=lambda var="HighlightsFrame":self.controller.prebaci_frejm(var))
		self.highlightsBtn.grid(row=0, column=1, padx=15, pady=5, sticky=W)

		Label(self, text="PRVO POLUVREME:").grid(row=0, column=2, padx=(0, 0), pady=5, sticky=E)

		self.entryPrvoPolMin = Entry(self, width=2)
		self.entryPrvoPolMin.grid(row=0, column=3, padx=(5, 2), pady=5, sticky=E)

		Label(self, text=":").grid(row=0, column=4, padx=(0, 0), pady=5, sticky=E)

		self.entryPrvoPolSec = Entry(self, width=2)
		self.entryPrvoPolSec.grid(row=0, column=5, padx=(2, 5), pady=5, sticky=E)

		##########

		Label(self, text="DRUGO POLUVREME:").grid(row=0, column=6, padx=(0, 0), pady=5, sticky=E)

		self.entryDrugoPolMin = Entry(self, width=2)
		self.entryDrugoPolMin.grid(row=0, column=7, padx=(5, 2), pady=5, sticky=E)

		Label(self, text=":").grid(row=0, column=8, padx=(0, 0), pady=5, sticky=E)

		self.entryDrugoPolSec = Entry(self, width=2)
		self.entryDrugoPolSec.grid(row=0, column=9, padx=(2, 5), pady=5, sticky=E)

		self.testBtn = Button(self, text="TEST",command=lambda var="TestFrame":self.controller.prebaci_frejm(var))
		self.testBtn.grid(row=1, column=0, padx=15, pady=5, sticky=W)

		self.runBtn = Button(self, text="RUN",command = self.runTry)
		self.runBtn.grid(row=1, column=1, padx=15, pady=5, sticky=W)

		self.entryPrvoPolMin.insert(0, "05")
		self.entryPrvoPolSec.insert(0, "09")

		self.entryDrugoPolMin.insert(0, "59")
		self.entryDrugoPolSec.insert(0, "40")


	def getPrvoPol(self):
		prvoPolStart = self.footballEditor.setPrvoPol(self.entryPrvoPolMin.get()+":"+self.entryPrvoPolSec.get())
		return prvoPolStart
	def getDrugoPol(self):
		drugoPolStart = self.footballEditor.setDrugoPol(self.entryDrugoPolMin.get() + ":" + self.entryDrugoPolSec.get())
		return drugoPolStart
	def runTry(self):
		video = self.footballEditor.checker.vremenaUSekundama
		print(len(video))
		if (str(type(video)) == "<class 'list'>"):
			for i in range(len(video)):
				pocetak = video[i][0]
				kraj = video[i][1]
				self.footballEditor.seckanje(i, pocetak, kraj)