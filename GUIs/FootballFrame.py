from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
import threading


class FootballFrame(Frame):

	def __init__(self, parent, controller,fe):
		Frame.__init__(self, parent)
		self.footballEditor = fe
		self.controller = controller
		self.grid(row=0, column=0, sticky=W)
		self.create_widgets()
		self.fajlDialog = filedialog
		self.visibleExtraFrame = False
		

	def startTRender(self):
		self.t_render = threading.Thread(target=self.runRender)
		self.t_render.start()
	def getTRender(self):
		return self.t_render.is_alive()

	def create_widgets(self):
		self.mecBtn = Button(self, text="MEC",font=("Courier", 15), command=lambda var=filedialog,frame=self: self.footballEditor.getPutanja(var,frame))
		self.mecBtn.grid(row=0, column=0, padx=15, pady=5, sticky=W)

		self.highlightsBtn = Button(self, text="HIGLIGHTS",font=("Courier", 15),command=lambda var="HighlightsFrame":self.controller.prebaci_frejm(var))
		self.highlightsBtn.grid(row=0, column=1, padx=15, pady=5, sticky=W)

		###### regular time frame
		self.addRegularTimeFrame()


		###test and run

		self.testBtn = Button(self, text="TEST",font=("Courier", 15),command=lambda var="TestFrame":self.controller.prebaci_frejm(var))
		self.testBtn.grid(row=1, column=0, padx=15, pady=5, sticky=W)
		self.testBtn.promenljiva = "TEST"

		self.runBtn = Button(self, text="RUN",font=("Courier", 15),command = self.startTRender)
		self.runBtn.grid(row=1, column=1, padx=15, pady=5, sticky=W)

		##### extra time
		self.addExtraTimeFrame()
		self.showOrHideExtraFrame(False)


	def addRegularTimeFrame(self):

		self.regularTimeFrame = Frame(self)
		self.regularTimeFrame.grid(row=0, column=2, sticky=E)

		Label(self.regularTimeFrame, text="PRVO POLUVREME:", font=("Courier", 15)).grid(row=0, column=0, padx=(0, 0),
																						pady=5, sticky=E)

		self.entryPrvoPolMin = Entry(self.regularTimeFrame, width=2, font=("Courier", 15))
		self.entryPrvoPolMin.grid(row=0, column=1, padx=(5, 2), pady=5, sticky=E)

		Label(self.regularTimeFrame, text=":", font=("Courier", 15)).grid(row=0, column=2, padx=(0, 0), pady=5,
																		  sticky=E)

		self.entryPrvoPolSec = Entry(self.regularTimeFrame, width=2, font=("Courier", 15))
		self.entryPrvoPolSec.grid(row=0, column=3, padx=(2, 5), pady=5, sticky=E)

		##########

		Label(self.regularTimeFrame, text="DRUGO POLUVREME:", font=("Courier", 15)).grid(row=0, column=4, padx=(0, 0),
																						 pady=5, sticky=E)

		self.entryDrugoPolMin = Entry(self.regularTimeFrame, width=2, font=("Courier", 15))
		self.entryDrugoPolMin.grid(row=0, column=5, padx=(5, 2), pady=5, sticky=E)

		Label(self.regularTimeFrame, text=":", font=("Courier", 15)).grid(row=0, column=6, padx=(0, 0), pady=5,
																		  sticky=E)

		self.entryDrugoPolSec = Entry(self.regularTimeFrame, width=2, font=("Courier", 15))
		self.entryDrugoPolSec.grid(row=0, column=7, padx=(2, 5), pady=5, sticky=E)

	def addExtraTimeFrame(self):



		self.extraTimeFrame = Frame(self)
		self.extraTimeFrame.grid(row=1, column=2, sticky=E, columnspan=20)

		labelExtraTime = Label(self.extraTimeFrame, text="EXTRA TIME |", font=("Courier", 15))
		labelExtraTime.grid(row=0, column=0, pady=5, sticky=W)

		Label(self.extraTimeFrame, text="PRVO POLUVREME:", font=("Courier", 15)).grid(row=0, column=1, padx=(0, 0),
																					  pady=5, sticky=W)

		self.entryExtraPrvoPolMin = Entry(self.extraTimeFrame, width=2, font=("Courier", 15))
		self.entryExtraPrvoPolMin.grid(row=0, column=2, padx=(5, 2), pady=5, sticky=E)

		Label(self.extraTimeFrame, text=":", font=("Courier", 15)).grid(row=0, column=3, padx=(0, 0), pady=5, sticky=E)

		self.entryExtraPrvoPolSec = Entry(self.extraTimeFrame, width=2, font=("Courier", 15))
		self.entryExtraPrvoPolSec.grid(row=0, column=4, padx=(2, 5), pady=5, sticky=E)

		####################

		Label(self.extraTimeFrame, text="DRUGO POLUVREME:", font=("Courier", 15)).grid(row=0, column=5, padx=(0, 0),
																					   pady=5, sticky=E)

		self.entryExtraDrugoPolMin = Entry(self.extraTimeFrame, width=2, font=("Courier", 15))
		self.entryExtraDrugoPolMin.grid(row=0, column=6, padx=(5, 2), pady=5, sticky=E)

		Label(self.extraTimeFrame, text=":", font=("Courier", 15)).grid(row=0, column=7, padx=(0, 0), pady=5, sticky=E)

		self.entryExtraDrugoPolSec = Entry(self.extraTimeFrame, width=2, font=("Courier", 15))
		self.entryExtraDrugoPolSec.grid(row=0, column=8, padx=(2, 5), pady=5, sticky=E)

	def get1st(self):
		recnik = {"minut":self.entryPrvoPolMin.get(),"sekunda":self.entryPrvoPolSec.get()}
		return recnik
	def get2nd (self):
		recnik = {"minut":self.entryDrugoPolMin.get(),"sekunda":self.entryDrugoPolSec.get()}
		return recnik
	def get1stExtra(self):
		recnik = {"minut":self.entryExtraPrvoPolMin.get(),"sekunda":self.entryExtraPrvoPolSec.get()}
		return recnik
	def get2ndExtra(self):
		recnik = {"minut":self.entryExtraDrugoPolMin.get(),"sekunda":self.entryExtraDrugoPolSec.get()}
		return recnik
	def runRender(self):
		if(self.footballEditor.canRun()):
			if(self.footballEditor.putanja!= ""):
				if(self.footballEditor.checkVremenaUSekundama()):
					video = self.footballEditor.vremenaUSekundama
					for i in range(len(video)):
						pocetak = video[i][0]
						kraj = video[i][1]
						self.footballEditor.seckanje(i, pocetak, kraj)
					self.footballEditor.mergeAll()
					self.footballEditor.vremenaUSekundama = []
					self.footballEditor.tested = False
					messagebox.showinfo('Renderovanje', 'Renderovanje zavrseno.')
					os.startfile(self.footballEditor.imeFoldera)
				elif(self.footballEditor.checkVremenaUSekundama() == False):
					messagebox.showinfo('Renderovanje', 'Ispravite highlights.')
				elif(self.footballEditor.checkVremenaUSekundama() == None):
					messagebox.showinfo('Renderovanje', 'Testirajte mec.')

			else:
				messagebox.showinfo('Renderovanje', 'Niste dodali fajl.')

		else:
			messagebox.showinfo('Renderovanje', 'Program i dalje nije spreman za render.')

	def showOrHideExtraFrame(self,option):
		if(option == True):
			self.extraTimeFrame.grid()
			self.visibleExtraFrame = True
		else:
			self.extraTimeFrame.grid_remove()
			self.visibleExtraFrame = False


