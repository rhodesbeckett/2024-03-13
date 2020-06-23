from tkinter import *
from tkinter.ttk import Separator
from PIL import Image, ImageTk
from editor.Seconds import *
import os
import cv2
import warnings
warnings.filterwarnings("ignore")
from tkinter import messagebox
class TestFrame(Frame):
	def __init__(self, parent, controller,fe):
		Frame.__init__(self, parent)
		self.footballEditor = fe
		self.sekundeObj = Seconds()
		self.controller = controller
		self.grid(row=0, column=0, sticky=W)
		self.create_widgets()
	def create_widgets(self):
		self.nazadBtn = Button(self,text="<",font=("Courier", 20),command=lambda var="FootballFrame": self.controller.prebaci_frejm(var))
		self.nazadBtn.grid(row=1,column = 0, padx=(5, 0),pady=5,sticky=W)

		Label(self,text="Utakmica", font=("Courier", 20)).grid(row=2,column = 0, sticky=W,padx=(5, 0))
		self.labelUtakmica = Label(self,text="", font=("Courier", 20))
		self.labelUtakmica.grid(row = 2 , column = 1, sticky = W)

		self.labelPrvoPoluvreme0 = Label(self, text="Prvo poluvreme", font=("Courier", 20))
		self.labelPrvoPoluvreme0.grid(row=3, column=0, padx=(5, 0), sticky=W)

		self.labelPrvoPoluvreme = Label(self, text="", font=("Courier", 20))
		self.labelPrvoPoluvreme.grid(row=3, column=1, sticky=W,columnspan=3)

		self.labelDrugoPoluvreme0 = Label(self, text="Drugo poluvreme", font=("Courier", 20))
		self.labelDrugoPoluvreme0.grid(row=4, column=0, sticky=W,padx=(5, 0))
		self.labelDrugoPoluvreme = Label(self, text="", font=("Courier", 20))
		self.labelDrugoPoluvreme.grid(row=4, column=1, sticky=W,columnspan=3)



		Label(self, text="Unesite neko vreme:", font=("Courier", 20)).grid(row=6, column=0, padx=(5, 0),sticky=W,columnspan = 3)

		self.addEntriesTestFrame()

		seperator = Separator(self,orient = VERTICAL)
		seperator.grid(row = 0 ,column = 5 , rowspan = 10 , sticky = NS)

		self.addTestPhoto()

		Label(self, text="Highlights:", font=("Courier", 20)).grid(row=8, column=0,padx=(5,0), sticky=W,columnspan = 3)
		self.labelHighlights = Label(self, text="", font=("Courier", 20))
		self.labelHighlights.grid(row=8, column=1, padx=(5, 0), columnspan = 3,sticky=W)

	def addEntriesTestFrame(self):
		self.testEntriesFrame = Frame(self)

		self.testEntriesFrame.grid(row=7, column=0, sticky=W)
		self.entryTestMin = Entry(self.testEntriesFrame, width=2, font=("Courier", 20))
		self.entryTestMin.grid(row=1, column=0, padx=(5, 2), pady=7, sticky=W)

		Label(self.testEntriesFrame, text=":", font=("Courier", 20)).grid(row=1, column=1, padx=(0, 5), pady=5, sticky=W)

		self.entryTestSec = Entry(self.testEntriesFrame, width=2, font=("Courier", 20))
		self.entryTestSec.grid(row=1, column=2, padx=(2, 5), pady=2, sticky=W)

		self.poluvremeLabelCheck = Label(self.testEntriesFrame, text="Poluvreme:", font=("Courier", 20))
		self.poluvremeLabelCheck.grid(row=1, column=3, padx=1, sticky=W)

		self.poluvremeVar = StringVar()
		self.poluvremeVar.set("prvo")

		self.radioBtnPrvo = Radiobutton(self.testEntriesFrame, text='1', font=("Courier", 20), value='prvo', variable=self.poluvremeVar)
		self.radioBtnPrvo.grid(
			row=1, column=4, sticky=W, columnspan=1, padx=2
		)
		self.radioBtnDrugo = Radiobutton(self.testEntriesFrame, text='2', font=("Courier", 20), value='drugo',
					variable=self.poluvremeVar)
		self.radioBtnDrugo.grid(
			row=1, column=5, sticky=W, columnspan=1, padx=2
		)

		self.btnCheck = Button(self.testEntriesFrame,text="Proveri",font=("Courier", 12) , command = self.proveriFajl)
		self.btnCheck.grid(row=2,column = 0, columnspan = 3,sticky = W,padx=(5, 0))

	def addTestPhoto(self):

		self.slikaLabel = Label(self)
		# slikaLabel = Label(self,text="NESTO")
		self.slikaLabel.grid(row = 0,column = 6,rowspan = 10,padx = 10 , pady = 10,sticky=NW)
	def checkMatch(self):
		putanja = self.footballEditor.getCurrentPutanja()

		if(os.path.exists(putanja)):
			self.labelUtakmica["text"] = "OK"
			self.labelUtakmica.bind("<Button-1>", lambda e: self.doNothing())
		else:
			self.labelUtakmica["text"] = "NOT OK"
			self.labelUtakmica.bind("<Button-1>", lambda e: self.controller.prebaci_frejm("FootballFrame"))
	def checkPoluvreme(self,first,second):
		#prvo
		prvoMinut = self.sekundeObj.convertToSeconds(first["minut"],"minut")
		prvoSekunda = self.sekundeObj.convertToSeconds(first["sekunda"],"sekunda")
		if(prvoMinut!= None and prvoSekunda != None):
			self.labelPrvoPoluvreme["text"] = "OK"
			self.labelPrvoPoluvreme.bind("<Button-1>", lambda e: self.doNothing())
			self.footballEditor.prvo_pol = prvoMinut+prvoSekunda
		else:
			self.labelPrvoPoluvreme["text"] = "NOT OK"
			self.labelPrvoPoluvreme.bind("<Button-1>", lambda e: self.controller.prebaci_frejm("FootballFrame"))
			self.footballEditor.prvo_pol = 0

		#drugo
		drugoMinut = self.sekundeObj.convertToSeconds(second["minut"],"minut")
		drugoSekunda = self.sekundeObj.convertToSeconds(second["sekunda"],"sekunda")

		if (drugoMinut != None and drugoSekunda != None):
			self.labelDrugoPoluvreme["text"] = "OK"
			self.footballEditor.drugo_pol = drugoMinut + drugoSekunda
			self.labelPrvoPoluvreme.bind("<Button-1>", lambda e: self.doNothing())

		else:
			self.labelDrugoPoluvreme["text"] = "NOT OK"
			self.labelPrvoPoluvreme.bind("<Button-1>", lambda e: self.controller.prebaci_frejm("FootballFrame"))
			self.footballEditor.drugo_pol = 0

	def checkHighlights(self,lista,stringVars):
		brojac = 0
		vremeUSekundama = []
		self.footballEditor.highlightsCounter = 0
		#time stamp sadrzi entries svaki put po 3
		timeStamp = []
		forAdd = True
		forAddCounter = 0

		toContinue = True


		# stringVars[varIndex].get()
		if(self.footballEditor.tipHighlightsa == "regularFull"):
			toContinue = True
		elif (self.footballEditor.tipHighlightsa == "firstRegular"):
			for i in range(len(stringVars)):
				if(stringVars[i] != None):
					if(stringVars[i].get()!="prvo"):
						toContinue = False
						print(stringVars[i].get())
						print(i)
						break

		elif (self.footballEditor.tipHighlightsa == "secondRegular"):
			for i in range(len(stringVars)):
				if (stringVars[i] != None):
					if(stringVars[i].get()!="drugo"):
						toContinue = False
						print(stringVars[i].get())
						print(i)
						# break

		if(toContinue == True):
			for i in lista:
				if (str(type(i)) == "<class 'tkinter.Entry'>"):
					brojac+=1
					timeStamp.append(i)
					if(brojac==3):
						self.footballEditor.highlightsCounter += 1
						pocetakMin = self.sekundeObj.convertToSeconds(timeStamp[0].get(),"minut")
						if(pocetakMin == None):
							timeStamp[0]["bg"] = "#ff6529"
							forAdd = False
						else:
							timeStamp[0]["bg"] = "#ffffff"
						pocetakSek = self.sekundeObj.convertToSeconds(timeStamp[1].get(),"sekunda")
						if(pocetakSek == None):
							timeStamp[1]["bg"] = "#ff6529"
							forAdd = False
						else:
							timeStamp[1]["bg"] = "#ffffff"
						krajSekunde = self.sekundeObj.convertToSeconds(timeStamp[2].get(),"sekunda")
						if (krajSekunde == None):
							timeStamp[2]["bg"] = "#ff6529"
							forAdd = False
						else:
							timeStamp[2]["bg"] = "#ffffff"

						brojac = 0
						if(forAdd == True):
							forAddCounter+=1

							if(not self.footballEditor.prvo_pol == 0 or not self.footballEditor.drugo_pol == 0):

								rbtnIndex = lista.index(i) + 2
								varIndex = str(lista[rbtnIndex]).split(".!")[5].split("radiobutton")[1]
								varIndex = int((int(varIndex) / 2) - 1)
								poluvreme = stringVars[varIndex].get()




								timeStamp[0]["bg"] = "#ffffff"
								timeStamp[1]["bg"] = "#ffffff"
								timeStamp[2]["bg"] = "#ffffff"
								if(poluvreme=="prvo"):
									pocetak = self.footballEditor.prvo_pol + (pocetakMin + pocetakSek)
									kraj = pocetak + krajSekunde
									del timeStamp
									timeStamp = []

								elif (poluvreme == "drugo"):
									pocetak = self.footballEditor.drugo_pol + (pocetakMin + pocetakSek) - 2700
									kraj = pocetak + krajSekunde
									del timeStamp
									timeStamp = []

								vremeUSekundama.append((pocetak,kraj))
								del timeStamp
								timeStamp = []
								self.footballEditor.tested = True
							else:
								del timeStamp
								timeStamp = []
						else:
							del timeStamp
							timeStamp = []


		self.footballEditor.vremenaUSekundama = vremeUSekundama

		if(self.footballEditor.canRun()):
			self.labelHighlights["text"] = "OK"
			self.footballEditor.tested = True
			self.labelHighlights.bind("<Button-1>", lambda e: self.doNothing())
		elif(forAddCounter == self.footballEditor.highlightsCounter and toContinue==True):
			self.labelHighlights["text"] = "OK BUT"
			self.labelHighlights.bind("<Button-1>", lambda e: self.controller.prebaci_frejm("FootballFrame"))

		else:
			self.labelHighlights["text"] = "NOT OK"
			self.labelHighlights.bind("<Button-1>", lambda e: self.controller.prebaci_frejm("HighlightsFrame"))







	def proveriFajl(self):
		putanja = self.footballEditor.getCurrentPutanja()
		if(putanja!= ""):
			ceoMec = cv2.VideoCapture(putanja)
			try:
				if not os.path.exists('slike'):
					os.makedirs('slike')
			except OSError:
				print('Error: Creating directory of data')
			name = './slike/frame' + '.jpg'

			minut = self.sekundeObj.convertToSeconds(self.entryTestMin.get(),"minut")
			sekunda = self.sekundeObj.convertToSeconds(self.entryTestSec.get(),"sekunda")

			#
			if(minut != None and sekunda != None):
				if(self.footballEditor.tipHighlightsa=="regularFull" and self.footballEditor.prvo_pol != 0 and self.footballEditor.drugo_pol != 0):
					poluvreme = self.poluvremeVar.get()
				else:
					poluvreme = self.footballEditor.tipHighlightsa
				sekunde = 0

				if(poluvreme == "prvo" or poluvreme == "firstRegular"):
					if(poluvreme=="prvo" and self.footballEditor.prvo_pol != 0 ):
						sekunde = self.footballEditor.prvo_pol + minut + sekunda
						print(sekunde)
					elif(poluvreme == "firstRegular"):
						if(self.footballEditor.prvo_pol == 0):
							sekunde = -1
						else:
							sekunde = self.footballEditor.prvo_pol + minut + sekunda

				elif(poluvreme == "drugo" or poluvreme == "secondRegular"):
					if (poluvreme == "drugo" and self.footballEditor.drugo_pol != 0):
						sekunde = self.footballEditor.drugo_pol + (minut + sekunda) - 2700
					elif(poluvreme == "secondRegular"):
						if (self.footballEditor.drugo_pol == 0):
							sekunde = -1
						else:
							sekunde = self.footballEditor.drugo_pol + (minut + sekunda) - 2700

				elif(poluvreme == "regularFull"):
					sekunde = -1
				frame_per_second = 1

				try:
					frame_per_second = ceoMec.get(cv2.CAP_PROP_FPS)
				except RuntimeWarning:
					print("greskaaaaa")


				if(frame_per_second!=0.0 and (sekunde!= -1 and sekunde != 0)):


					frejm = int(frame_per_second * sekunde)
					ukupnoFrejmova = int(ceoMec.get(cv2.CAP_PROP_FRAME_COUNT))
					self.footballEditor.ceoMecSekunde =  int(ukupnoFrejmova/frame_per_second)
					if(not frejm>ukupnoFrejmova):
						ceoMec.set(1, frejm)

						ret, frame = ceoMec.read()
						cv2.imwrite(name, frame)
						ceoMec.release()
						cv2.destroyAllWindows()

						slika = Image.open("./slike/frame.jpg")
						slika = slika.resize((651,305),Image.ANTIALIAS)
						self.testImg = ImageTk.PhotoImage(slika)
						self.slikaLabel["image"] = self.testImg
				else:
					if(sekunde == -1):
						messagebox.showinfo('Test','Nedostaje vam poluvreme.')
					else:
						messagebox.showinfo('Test', 'Pogresan file format.')
			else:
				messagebox.showinfo('Test', 'Pogresan time format ili poluvreme nije postavljeno.')
		else:
			messagebox.showinfo('Test', 'Niste dodali fajl.')
	def doNothing(self):
		return None
	def hidePoluvremeWidgets(self, poluvreme):

		if(poluvreme == "prvo"):
			self.labelPrvoPoluvreme.grid()
			self.labelDrugoPoluvreme.grid_remove()

			self.labelPrvoPoluvreme0.grid()
			self.labelDrugoPoluvreme0.grid_remove()

			self.radioBtnPrvo.grid_remove()
			self.radioBtnDrugo.grid_remove()
			self.poluvremeLabelCheck.grid_remove()

		elif(poluvreme == "drugo"):
			self.labelDrugoPoluvreme.grid()
			self.labelPrvoPoluvreme.grid_remove()

			self.labelDrugoPoluvreme0.grid()
			self.labelPrvoPoluvreme0.grid_remove()

			self.radioBtnPrvo.grid_remove()
			self.radioBtnDrugo.grid_remove()
			self.poluvremeLabelCheck.grid_remove()

		elif(poluvreme == "full"):
			self.labelPrvoPoluvreme.grid()
			self.labelDrugoPoluvreme.grid()

			self.labelPrvoPoluvreme0.grid()
			self.labelDrugoPoluvreme0.grid()

			self.radioBtnPrvo.grid()
			self.radioBtnDrugo.grid()
			self.poluvremeLabelCheck.grid()
