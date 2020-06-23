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

	def startTRender(self):
		self.t_render = threading.Thread(target=self.runRender)
		self.t_render.start()
	def getTRender(self):
		return self.t_render.is_alive()
	def startTCut(self):
		self.t_cut = threading.Thread(target= lambda var=True:self.runCut(var))
		self.t_cut.start()

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


		self.footballEditor.tipHighlightsa = "regularFull"



		self.frameForCut = Frame(self)
		self.frameForCut.grid(row=1, column=2,sticky=W)

		self.justCut = Button(self.frameForCut, text="JUST CUT", font=("Courier", 15), command=self.startTCut)
		self.justCut.grid(row=0, column=0, padx=1, pady=5, sticky=W)

		Label(self.frameForCut,text="FOLDER:", font=("Courier", 15)).grid(row=0, column=1, padx=15, pady=5,sticky=E)

		self.entryVideosLocation= Entry(self.frameForCut, width=15, font=("Courier", 15))
		self.entryVideosLocation.grid(row=0, column=2, padx=(5, 2), pady=5, sticky=E)

		self.showOrHideFrameForCut(False)

	def getVideoLocation(self):
		lokacija = self.entryVideosLocation.get()
		return lokacija

	def showOrHideFrameForCut(self,var):
		if(var==True):
			self.frameForCut.grid()
		else:
			self.frameForCut.grid_remove()


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


	def get1st(self):
		recnik = {"minut":self.entryPrvoPolMin.get(),"sekunda":self.entryPrvoPolSec.get()}
		return recnik

	def get2nd (self):
		recnik = {"minut":self.entryDrugoPolMin.get(),"sekunda":self.entryDrugoPolSec.get()}
		return recnik

	def runRender(self):
		###
		if(self.footballEditor.canRun()):
			if(self.footballEditor.getCurrentPutanja()!= ""):
				if(self.footballEditor.checkVremenaUSekundama()):
					self.runCut(False)
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


	def runCut(self,provera):
		checkVar = False
		#ne treba provera posto je u run render
		if(provera==False):
			checkVar = True
		#treba provera postoje u run cut
		elif(provera == True):
			if (self.footballEditor.canRun()):
				if (self.footballEditor.getCurrentPutanja() != ""):
					if (self.footballEditor.checkVremenaUSekundama()):
						checkVar = True

					elif (self.footballEditor.checkVremenaUSekundama() == False):
						messagebox.showinfo('Renderovanje', 'Ispravite highlights.')
						checkVar = False

					elif (self.footballEditor.checkVremenaUSekundama() == None):
						messagebox.showinfo('Renderovanje', 'Testirajte mec.')
						checkVar = False
				else:
					messagebox.showinfo('Renderovanje', 'Niste dodali fajl.')
					checkVar = False
			else:
				messagebox.showinfo('Renderovanje', 'Program i dalje nije spreman za render.')
				checkVar = False
		#ako je tacna provera onda moze cut da pocne
		if(checkVar == True):
			forRun2 = True
			if (self.footballEditor.tipHighlightsa in ("firstRegular", "secondRegular")):

				lokacijaVideaa = self.getVideoLocation()
				# ako je prazno onda reci da je greska u pitanju
				if (lokacijaVideaa == "" or lokacijaVideaa == None):
					messagebox.showinfo('Renderovanje', 'Niste naveli ime foldera.')
					forRun2 = False
				elif (lokacijaVideaa != "" or lokacijaVideaa != None):
					self.footballEditor.napraviFolder(lokacijaVideaa)
					forRun2 = True
			else:
				self.footballEditor.napraviFolder("")
				forRun2 = True

			if (forRun2 == True):

				iCounter = self.footballEditor.getInfoAboutVideos("len")
				video = self.footballEditor.vremenaUSekundama
				for i in range(len(video)):
					pocetak = video[i][0]
					kraj = video[i][1]
					seckanje = self.footballEditor.seckanje(iCounter, pocetak, kraj)
					if(seckanje == None):
						iCounter += 1
				if(provera == True):
					messagebox.showinfo('Cut', 'Cut je uspesno zavrsen.')
		print("cut")

	def getHighlightsType(self):
		return self.footballEditor.tipHighlightsa
	# def splitVideos(self):

