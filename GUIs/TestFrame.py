import os
import warnings
from tkinter import *
from tkinter.ttk import Separator

import cv2
from PIL import Image, ImageTk

from editor.Seconds import *

warnings.filterwarnings("ignore")
from tkinter import messagebox
from utils.Pregledanje import *
from utils.Testing import Testing
from utils.tkw.TKWIdgets import TKWidgets


class TestFrame(Frame):
	def __init__(self, parent, controller, fe):
		Frame.__init__(self, parent)
		self.footballEditor = fe
		self.sekundeObj = Seconds()
		self.test = Testing(self)
		self.tkw = TKWidgets(self)
		self.tkw.set_font(("Courier", 20))
		self.controller = controller
		self.grid(row=0, column=0, sticky=W)
		self.create_widgets()

	def create_widgets(self):
		# 0 0
		# font=("Courier", 20)
		data = self.tkw.setData("<", padx=(5, 0), pady=5, sticky=W)
		self.tkw.insert(Button, 0, data)
		self.tkw.set("command", lambda var="FootballFrame": self.controller.prebaci_frejm(var), 0, 0)
		self.tkw.add_new_row(0)
		# 0 1
		data = self.tkw.setData("Utakmica", padx=(5, 0), pady=0, sticky=W)
		self.tkw.insert(Label, 0, data)
		# 0 2
		data = self.tkw.setData(" ", sticky=W)
		self.tkw.insert(Label, 0, data)
		self.tkw.add_new_row(0)
		# 0 3
		data = self.tkw.setData("Prvo poluvreme", padx=(5, 0), pady=0, sticky=W)
		self.tkw.insert(Label, 0, data)
		# 0 4
		data = self.tkw.setData(" ", padx=(0, 0), pady=0, columnspan=3, sticky=W)
		self.tkw.insert(Label, 0, data)
		self.tkw.add_new_row(0)
		# 0 5
		data = self.tkw.setData("Drugo poluvreme", padx=(5, 0), pady=0, sticky=W)
		self.tkw.insert(Label, 0, data)
		# 0 6
		data = self.tkw.setData(" ", padx=0, pady=0, columnspan=3, sticky=W)
		self.tkw.insert(Label, 0, data)
		self.tkw.add_new_row(0)
		# 0 7
		data = self.tkw.setData("Unesite neko vreme:", padx=(5, 0), pady=0, columnspan=3, sticky=W)
		self.tkw.insert(Label, 0, data)
		self.tkw.add_new_row(0)

		self.addEntriesTestFrame()

		# 0 9
		data = self.tkw.setData(None, rowspan=10, sticky=NS)
		self.tkw.insert(Separator, 0, data)
		self.tkw.set("orient", VERTICAL, 0, 9)
		self.tkw.set_specific_grid(0, 9, 0, 5)
		# 0 10
		self.addTestPhoto()
		# 0 11
		self.tkw.add_new_row(0)
		data = self.tkw.setData("Highlights:", padx=(5, 0), sticky=W, columnspan=3)
		self.tkw.insert(Label, 0, data)
		# self.tkw.addNewRow(0)
		# # 0 12
		data = self.tkw.setData(" ", padx=(5, 0), columnspan=2, sticky=W)
		self.tkw.insert(Label, 0, data)
		print("gotovo")



	def addEntriesTestFrame(self):
		# 0 8
		data = self.tkw.setData("", sticky=W)
		self.tkw.insert(Frame, 0, data,True)

		# 1 0
		data = self.tkw.setData(" ", padx=(5, 2), pady=7, sticky=W)
		self.tkw.insert(Entry, 1, data)
		self.tkw.set("width", 2, 1, 0)
		# 1 1
		data = self.tkw.setData(":", padx=(0, 5), pady=5, sticky=W)
		self.tkw.insert(Label, 1, data)
		# 1 2
		data = self.tkw.setData(" ", padx=(2, 5), pady=2, sticky=W)
		self.tkw.insert(Entry, 1, data)
		self.tkw.set("width", 2, 1, 2)
		# 1 3
		data = self.tkw.setData("Poluvreme:", sticky=W)
		self.tkw.insert(Label, 1, data)

		self.poluvremeVar = StringVar()
		self.poluvremeVar.set("prvo")
		# 1 4
		data = self.tkw.setData("1", padx=2, sticky=W, columnspan=1)
		self.tkw.insert(Radiobutton, 1, data)
		self.tkw.set("value", "prvo", 1, 4)
		self.tkw.set("variable", self.poluvremeVar, 1, 4)
		# 1 5
		data = self.tkw.setData("2", columnspan=1, sticky=W, padx=2)
		self.tkw.insert(Radiobutton, 1, data)

		self.tkw.set("value", "drugo", 1, 5)
		self.tkw.set("variable", self.poluvremeVar, 1, 5)

		# 1 6
		self.tkw.add_new_row(1)

		data = self.tkw.setData("Proveri", columnspan = 3, sticky = W, padx=(5, 0))
		self.tkw.insert(Button, 1, data)
		self.tkw.set("command", self.proveriFajl, 1, 6)
		self.tkw.set("font", ("Courier", 12), 1, 6)

	def addTestPhoto(self):
		# 0 10
		data = self.tkw.setData("", rowspan = 10, padx = 10, pady = 10, sticky=NW, row=0, column=7)
		self.tkw.insert(Label,0,data)
		# self.tkw.setSpecificGrid(0, 10, 0, 55)

		# Label(self,text="aa\n"*15).grid(row=0,column=6,rowspan = 10,padx = 10 , pady = 10,sticky=NW)
	# slikaLabel = Label(self,text="NESTO")

	def checkHighlights(self, lista, stringVars):
		vremeUSekundama, timeStamp, forAdd, testirano = self.test.initVarsForChecking()

		if proveraTipa(self, "firstRegular"):
			if not getToContinue("prvo", stringVars):
				testirano = "ne"
				return None
		elif proveraTipa(self, "secondRegular"):
			if not getToContinue("drugo", stringVars):
				testirano = "ne"
				return None

		# HIGHLIGHTS IMA PRAVILNE UNOSE ZA POLUVREME
		for i in lista:
			if daLiJeEntry(i):
				timeStamp.append(i)
				if len(timeStamp) == 3:
					forAdd, red = self.test.koloneTest(timeStamp)
					# OVAJ TIMESTAMP JE TACAN
					if forAdd == True:
						rbtnIndex = lista.index(i) + 2
						poluvreme = getPoluvremeFromRButton(self.controller.prozori["HighlightsFrame"], lista,
															rbtnIndex, "objekat")
						paint(timeStamp)
						if poluvreme in ("prvo", "drugo"):
							pocetak = calculatePocetak(self, red["minut"], red["sekunda"], poluvreme)
							kraj = calculateKraj(pocetak, red["add"])
							timeStamp = []
							vremeUSekundama.append((pocetak, kraj))
					else:
						timeStamp = []

		if self.test.brojRedove(lista) == len(vremeUSekundama):
			if isPoluvreme12NotNula(self):
				self.footballEditor.highlightsCounter = self.test.brojRedove(lista)
				self.footballEditor.vremenaUSekundama = vremeUSekundama
				testirano = "uspesno"
			else:
				testirano = "ali"
		# AKO JE USPESNO TESTIRANO ONDA MOZE RUN
		if testirano == "uspesno":
			self.footballEditor.vremenaUSekundama = vremeUSekundama
			setLabel(self, self.doNothing, "OK", True)
		# AKO JE TESTIRANO ALI NEMA PRVO ILI DRUGO POLUVREME
		elif testirano == "ali":
			setLabel(self, self.controller.prebaci_frejm, "OK BUT", False)
		# AKO JE TESTIRANO NE
		else:
			setLabel(self, self.controller.prebaci_frejm, "NOT OK", False)

	def proveriFajl(self):
		putanja = self.footballEditor.getCurrentPutanja()
		if putanja != "":
			ceoMec = cv2.VideoCapture(putanja)
			try:
				if not os.path.exists('slike'):
					os.makedirs('slike')
			except OSError:
				print('Error: Creating directory of data')
			name = './slike/frame' + '.jpg'

			minut = self.sekundeObj.convertToSeconds(self.tkw.get_object(1, 0).get(), "minut")
			sekunda = self.sekundeObj.convertToSeconds(self.tkw.get_object(1, 2).get(), "sekunda")

			#
			if minut != None and sekunda != None:
				if (
									self.footballEditor.tipHighlightsa == "regularFull" and self.footballEditor.prvo_pol != 0 and self.footballEditor.drugo_pol != 0):
					poluvreme = self.poluvremeVar.get()
				else:
					poluvreme = self.footballEditor.tipHighlightsa
				sekunde = 0

				if poluvreme == "prvo" or poluvreme == "firstRegular":
					if poluvreme == "prvo" and self.footballEditor.prvo_pol != 0:
						sekunde = self.footballEditor.prvo_pol + minut + sekunda
						print(sekunde)
					elif poluvreme == "firstRegular":
						if self.footballEditor.prvo_pol == 0:
							sekunde = -1
						else:
							sekunde = self.footballEditor.prvo_pol + minut + sekunda

				elif poluvreme == "drugo" or poluvreme == "secondRegular":
					if poluvreme == "drugo" and self.footballEditor.drugo_pol != 0:
						sekunde = self.footballEditor.drugo_pol + (minut + sekunda) - 2700
					elif poluvreme == "secondRegular":
						if self.footballEditor.drugo_pol == 0:
							sekunde = -1
						else:
							sekunde = self.footballEditor.drugo_pol + (minut + sekunda) - 2700

				elif poluvreme == "regularFull":
					sekunde = -1
				frame_per_second = 1

				try:
					frame_per_second = ceoMec.get(cv2.CAP_PROP_FPS)
				except RuntimeWarning:
					print("greskaaaaa")

				if frame_per_second != 0.0 and (sekunde != -1 and sekunde != 0):

					frejm = int(frame_per_second * sekunde)
					ukupnoFrejmova = int(ceoMec.get(cv2.CAP_PROP_FRAME_COUNT))
					self.footballEditor.ceoMecSekunde = int(ukupnoFrejmova / frame_per_second)
					if not frejm > ukupnoFrejmova:
						ceoMec.set(1, frejm)

						ret, frame = ceoMec.read()
						cv2.imwrite(name, frame)
						ceoMec.release()
						cv2.destroyAllWindows()

						slika = Image.open("./slike/frame.jpg")
						slika = slika.resize((651, 305), Image.ANTIALIAS)
						self.testImg = ImageTk.PhotoImage(slika)
						self.tkw.set("image", self.testImg, 0, 10)
				else:
					if sekunde == -1:
						messagebox.showinfo('Test', 'Nedostaje vam poluvreme.')
					else:
						messagebox.showinfo('Test', 'Pogresan file format.')
			else:
				messagebox.showinfo('Test', 'Pogresan time format ili poluvreme nije postavljeno.')
		else:
			messagebox.showinfo('Test', 'Niste dodali fajl.')

	def doNothing(self):
		return None

	def hidePoluvremeWidgets(self, poluvreme):
		firstFrame = self.winfo_children()
		secondFrame = self.tkw.get_parent(1).winfo_children()
		hidePoluvreme(poluvreme, firstFrame, secondFrame)

	def checkAll(self, prvo, drugo, allElements, stringVars):
		self.test.match()
		# PROVERA FORMATA POLUVREMENA
		self.test.poluvremena(prvo, drugo)
		# PROVERA PREGLEDA
		self.checkHighlights(allElements, stringVars)

	def setFrame(self, frame):
		self.test.frame = frame
