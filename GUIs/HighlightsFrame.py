from tkinter import *
from tkinter import filedialog as fileDialog
import re
import os
from tkinter import messagebox
import random

class HighlightsFrame(Frame):
	def __init__(self, parent, controller,fe):
		Frame.__init__(self, parent)
		self.footballEditor = fe
		self.controller = controller
		self.grid(row=0, column=0, sticky=W)
		self.columnH = 0
		self.rowH = 0
		self.tabKey = Event
		self.stringVars = []
		self.defaultVar = "prvo"
		self.scrollbar_setup()
		self.create_widgets()

	def scrollbar_setup(self):
		self.canvas = Canvas(self, borderwidth=0)
		self.frame = Frame(self.canvas)
		self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)
		# recnik = {'link0': ['slika1', 'slika2']}}

		self.vsb.pack(side="right", fill="y")
		self.canvas.pack(side="left", fill="both", expand=True)
		self.canvas.create_window((4, 4), window=self.frame, anchor="nw",
								  tags="self.frame")

		self.frame.bind("<Configure>", self.onFrameConfigure)
		self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

	def _on_mousewheel(self, event):
		self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

	def onFrameConfigure(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))

	def create_widgets(self):

		self.addMenu()

		self.addBackButton()

		self.addRow()

	def addRow(self):
		self.rowH += 1

		labelPocetak = Label(self.frame, text="Pocetak", font=("Courier", 20))
		labelPocetak.grid(row=self.rowH, column=0, padx=(0, 0), pady=5, sticky=W)
		self.columnH += 1

		self.entryPrvoPolMin = Entry(self.frame, width=2, font=("Courier", 20))
		self.entryPrvoPolMin.grid(row=self.rowH, column=self.columnH, padx=(5, 2), pady=5, sticky=W)
		self.columnH += 1

		Label(self.frame, text=":", font=("Courier", 20)).grid(row=self.rowH, column=self.columnH, padx=(0, 0), pady=5,
															   sticky=W)
		self.columnH += 1

		self.entryPrvoPolSec = Entry(self.frame, width=2, font=("Courier", 20))
		self.entryPrvoPolSec.grid(row=self.rowH, column=self.columnH, padx=(2, 5), pady=5, sticky=W)
		self.columnH += 1

		##########

		Label(self.frame, text="+", font=("Courier", 20)).grid(row=self.rowH, column=self.columnH, padx=(0, 0),
																  pady=5, sticky=W)
		self.columnH += 1

		self.entryPlus = Entry(self.frame, width=2, font=("Courier", 20))
		self.entryPlus.grid(row=self.rowH, column=self.columnH, padx=(5, 2), pady=5, sticky=W)
		self.columnH += 1

		self.poluvremeVar = StringVar()
		self.poluvremeVar.set(self.defaultVar)
		self.stringVars.append(self.poluvremeVar)

		Radiobutton(self.frame, text='Prvo poluvreme', font=("Courier", 20),value='prvo', variable=self.stringVars[-1], command=lambda var=self.stringVars[-1]: self.getPoluvreme(var)).grid(
			row=self.rowH, column=self.columnH, sticky=W
		)
		self.columnH += 1
		Radiobutton(self.frame, text='Drugo poluvreme', font=("Courier", 15), value='drugo', variable=self.stringVars[-1], command=lambda var=self.stringVars[-1]: self.getPoluvreme(var)).grid(
			row=self.rowH, column=self.columnH, sticky=W
		)

		self.columnH += 1

		# print("POSLEDNJI : " + str(self.getLastRadioBtn()))
		lastRadioBtn = self.getLastRadioBtn()
		self.deleteBtn = Button(self.frame,text="Obrisi",font=("Courier", 20))
		self.deleteBtn["command"] = lambda var1=self.getLastRadioBtn(),var2=self.stringVars.index(self.stringVars[-1]):self.deleteRow(var1,var2)
		self.deleteBtn.grid(row=self.rowH,column = self.columnH,sticky = W)
		self.columnH = 0

	def getLista(self):
		return self.frame.winfo_children()[:-12:-1]

	def clickOnTab(self):
		lista = self.getLista()
		brojac = 0
		radioBtns = []
		for i in lista:
			# <class 'tkinter.Radiobutton'>
			if (str(type(i)) == "<class 'tkinter.Entry'>"):
				if (len(i.get()) > 0):
					brojac += 1
			elif(str(type(i)) == "<class 'tkinter.Radiobutton'>"):
				radioBtns.append(i)

		lastRadio = -1
		if (brojac == 3):
			while(True):
				try:
					vrednost = self.stringVars[lastRadio].get()
					self.defaultVar = vrednost
					self.addRow()
					self.getLista()[7].focus()
					break
				except:
					lastRadio-=1
					continue


	def setTabKeyPress(self, event):
		try:
			if (str(self.char) == 0):
				self.tabKey = event
				print("postavljeno")
		except:
			self.tabKey = event
			print("postavljeno2")

	def getAllElements(self):
		return self.frame.winfo_children()

	def getPoluvreme(self,var):
		return var.get()

	def removeG(self,slovo):
		lista = self.getAllElements()
		for i in lista:
			if (str(type(i)) == "<class 'tkinter.Entry'>"):
				value = i.get()
				value2 = re.sub("[a-zA-Z]", "", value)
				try:
					int(value2)
				except:
					value2 = ""

				i.delete(0,END)
				i.insert(0, value2)

	def deleteRow(self,lastRadioBtn,stringVarIndex):
		lastRadioBtnIndex = self.getAllElements().index(lastRadioBtn)
		startIndex = lastRadioBtnIndex-7
		deleteBtnIndex = startIndex+8

		templista = self.getAllElements()
		for i in range(startIndex,deleteBtnIndex+1):
			templista[i].destroy()

		# self.stringVars[stringVarIndex] = None
		self.stringVars[stringVarIndex] = None
	def getLastRadioBtn(self):
		lastRadioBtn = self.getAllElements()[-2]
		# br = int(lastRadioBtn.split(".!")[5].split("radiobutton")[1])
		# return br
		return lastRadioBtn
	def addBackButton(self):
		self.backButton = Button(self.frame, text="<", font=("Courier", 20),command=self.goBack)
		self.backButton.grid(row=0, column=0, padx=(5, 2), pady=5, sticky=W)
	def addMenu(self):

		menubar = Menu(self.frame)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Open",command = self.checkFileEntries)
		filemenu.add_command(label="Save",command = self.saveToFile)
		filemenu.add_separator()
		filemenu.add_command(label="Exit",command = self.closeApp)
		menubar.add_cascade(label="File", menu=filemenu)
		self.controller.config(menu=menubar)
	def goBack(self):
		self.controller.prebaci_frejm("FootballFrame")
	def saveToFile(self):
		if(self.controller.page_name=="HighlightsFrame"):
			#ovde ce trebati metoda za otvaranje foldera za upload
			imeTempFajla = "highlights"+str(random.randint(1,1000))+".txt"
			fajl = open(imeTempFajla,"w",encoding="utf-8")
			templista = self.getAllElements()[:]
			brojac = 0
			row = []
			for i in templista:
				if (str(type(i)) == "<class 'tkinter.Entry'>"):
					brojac+=1
					row.append(i)
					if(brojac==3):
						rbtnIndex = templista.index(i) + 2
						varIndex = str(templista[rbtnIndex]).split(".!")[5].split("radiobutton")[1]
						varIndex = int((int(varIndex) / 2) - 1)
						poluvreme = self.stringVars[varIndex].get()

						minut = row[0].get()
						sekunda = row[1].get()
						end = row[2].get()

						if(minut==""):
							minut = "0"
						if(sekunda == ""):
							sekunda = "0"
						if(end == ""):
							end = "0"

						rowFile = minut + " " + sekunda + " " + end + " " + poluvreme + "\n"
						fajl.write(rowFile)
						brojac = 0
						row = []
			fajl.close()
	def removeAllEntries(self):
		lista = self.getAllElements()
		exceptions = [".!frame.!highlightsframe.!canvas.!frame.!menu",".!frame.!highlightsframe.!canvas.!frame.!button"]
		for i in lista:
			if(str(i) not in exceptions):
				i.destroy()
	def checkFileEntries(self):
		if(self.controller.page_name=="HighlightsFrame"):
			highlightsPutanja = ""
			extt = ""
			try:
				if (str(type(fileDialog)) == "<class 'module'>"):
					rep = fileDialog.askopenfilename(
						parent=self.frame,
						initialdir='/',
						initialfile='tmp',
						filetypes=[
							("All files", "*")])
					highlightsPutanja = rep
					extt = os.path.splitext(str(highlightsPutanja))[1]
			except Exception as e:
				print("greska: " + str(e))


			if(highlightsPutanja != "" and extt == ".txt"):
				sablon = re.compile(r'(.*\s.*\s.*(\sprvo|drugo))')
				fajl = open(highlightsPutanja,"r",encoding="utf-8")
				linija = fajl.readline()
				redovi = []
				while(linija!=""):
					pretraga = sablon.findall(linija)
					if(len(pretraga)>0):
						if(len(pretraga[0])>0):
							forEntries = pretraga[0][0].split(" ")
							redovi.append([forEntries[0],forEntries[1],forEntries[2],forEntries[3].split("\n")[0]])
							linija = fajl.readline()
						else:
							messagebox.showinfo('Highlights load', 'Pogresan format za highlights.')
							fajl.close()
							break
					else:
						messagebox.showinfo('Highlights load', 'Pogresan format za highlights.')
						fajl.close()
						pretraga = []
						break


				if(not pretraga == []):
					self.removeAllEntries()
					for i in range(len(redovi)):
						self.addRow()

					lista = self.getAllElements()
					red = -1
					brojac = 0
					entries = []

					for i in range(len(lista)):
						if (str(type(lista[i])) == "<class 'tkinter.Entry'>"):
							brojac+=1
							entries.append(lista[i])
							if(brojac==3):
								red+=1
								entries[0].insert(0,redovi[red][0])
								entries[1].insert(0,redovi[red][1])
								entries[2].insert(0,redovi[red][2])

								rbtnIndex = lista.index(lista[i]) + 2
								varIndex = str(lista[rbtnIndex]).split(".!")[5].split("radiobutton")[1]
								varIndex = int((int(varIndex) / 2) - 1)

								self.stringVars[varIndex].set(redovi[red][3].split("\n")[0])
								# print(self.stringVars[varIndex])

								entries = []
								brojac = 0
				else:
					messagebox.showinfo('Highlights load', 'Ispravite greske u highlights txt da bi ste uspesno ucitali.')
			else:
				messagebox.showinfo('Highlights load', 'txt fajl format je neophodan.')
	def closeApp(self):
		self.saveToFile()
		self.controller.quit()