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

	def create_widgets(self):
		self.mecBtn = Button(self, text="MEC",font=("Courier", 15), command=lambda var=filedialog,frame=self: self.footballEditor.getPutanja(var,frame))
		self.mecBtn.grid(row=0, column=0, padx=15, pady=5, sticky=W)

		self.highlightsBtn = Button(self, text="HIGLIGHTS",font=("Courier", 15),command=lambda var="HighlightsFrame":self.controller.prebaci_frejm(var))
		self.highlightsBtn.grid(row=0, column=1, padx=15, pady=5, sticky=W)

		Label(self, text="PRVO POLUVREME:",font=("Courier", 15)).grid(row=0, column=2, padx=(0, 0), pady=5, sticky=E)

		self.entryPrvoPolMin = Entry(self, width=2,font=("Courier", 15))
		self.entryPrvoPolMin.grid(row=0, column=3, padx=(5, 2), pady=5, sticky=E)

		Label(self, text=":",font=("Courier", 15)).grid(row=0, column=4, padx=(0, 0), pady=5, sticky=E)

		self.entryPrvoPolSec = Entry(self, width=2,font=("Courier", 15))
		self.entryPrvoPolSec.grid(row=0, column=5, padx=(2, 5), pady=5, sticky=E)

		##########

		Label(self, text="DRUGO POLUVREME:",font=("Courier", 15)).grid(row=0, column=6, padx=(0, 0), pady=5, sticky=E)

		self.entryDrugoPolMin = Entry(self, width=2,font=("Courier", 15))
		self.entryDrugoPolMin.grid(row=0, column=7, padx=(5, 2), pady=5, sticky=E)

		Label(self, text=":",font=("Courier", 15)).grid(row=0, column=8, padx=(0, 0), pady=5, sticky=E)

		self.entryDrugoPolSec = Entry(self, width=2,font=("Courier", 15))
		self.entryDrugoPolSec.grid(row=0, column=9, padx=(2, 5), pady=5, sticky=E)

		self.testBtn = Button(self, text="TEST",font=("Courier", 15),command=lambda var="TestFrame":self.controller.prebaci_frejm(var))
		self.testBtn.grid(row=1, column=0, padx=15, pady=5, sticky=W)

		self.runBtn = Button(self, text="RUN",font=("Courier", 15),command = self.startTRender)
		self.runBtn.grid(row=1, column=1, padx=15, pady=5, sticky=W)


	def get1st(self):
		recnik = {"minut":self.entryPrvoPolMin.get(),"sekunda":self.entryPrvoPolSec.get()}
		return recnik
	def get2nd (self):
		recnik = {"minut":self.entryDrugoPolMin.get(),"sekunda":self.entryDrugoPolSec.get()}
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
				else:
					messagebox.showinfo('Renderovanje', 'Ispravite highlights.')
			else:
				messagebox.showinfo('Renderovanje', 'Niste dodali fajl.')

		else:
			messagebox.showinfo('Renderovanje', 'Program i dalje nije spreman za render.')
