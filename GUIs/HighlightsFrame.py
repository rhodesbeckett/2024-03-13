import os
from tkinter import *
from tkinter import filedialog as fileDialog
from tkinter import messagebox

from utils.Pregledanje import *
from utils.tkw.TKWIdgets import TKWidgets


class HighlightsFrame(Frame):
	def __init__(self, parent, controller, fe):
		Frame.__init__(self, parent)
		self.footballEditor = fe
		self.controller = controller
		self.grid(row=0, column=0, sticky=W)
		self.columnH = 0
		self.rowH = 0
		self.tabKey = Event
		self.stringVars = []
		self.defaultVar = "prvo"
		self.imeTxtFajla = ""
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
		self.tkw = TKWidgets(self.frame)

	def _on_mousewheel(self, event):
		self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

	def onFrameConfigure(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))

	def create_widgets(self):

		self.addMenu()

		self.addBackButton()

		self.addRow()

	def addMenu(self):

		menubar = Menu(self.frame)
		filemenu = Menu(menubar, tearoff=0)
		filemenu.add_command(label="Open", command=self.checkFileEntries)
		filemenu.add_command(label="Save", command=self.saveToFile)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.closeApp)
		menubar.add_cascade(label="File", menu=filemenu)

		# za meceve
		matchesmenu = Menu(menubar, tearoff=0)
		matchesmenu.add_command(label="Only first regular", command=self.setFirstReg)
		matchesmenu.add_command(label="Only second regular", command=self.setSecondtReg)
		matchesmenu.add_command(label="Regular one part", command=self.setFullReg)
		menubar.add_cascade(label="Matches", menu=matchesmenu)

		# za audio
		audioMenu = Menu(menubar, tearoff=0)
		audioMenu.add_command(label="Disable audio", command=lambda var=False: self.setAudio(var))
		audioMenu.add_command(label="Enable audio", command=lambda var=True: self.setAudio(var))
		menubar.add_cascade(label="Audio", menu=audioMenu)

		# za video
		videoMenu = Menu(menubar, tearoff=0)
		videoMenu.add_command(label="Source extension", command=lambda var="": self.setExt(var))
		videoMenu.add_command(label="MP4 extension", command=lambda var=".mp4": self.setExt(var))
		menubar.add_cascade(label="Video", menu=videoMenu)

		self.controller.config(menu=menubar)

	def addBackButton(self):
		# 0 1
		self.tkw.set_font(("Courier", 20))
		data = self.tkw.setData(text="<", padx=(5, 2), pady=5, sticky=W)
		self.tkw.insert(Button,0,data)
		self.tkw.set("command", self.goBack)

	def addRow(self):
		self.tkw.add_new_row(0)
		# 0 2
		data = self.tkw.setData(text="Pocetak", padx=(5, 2), pady=5, sticky=W)
		self.tkw.insert(Label, 0, data)

		# 0 3
		self.tkw.set_font(("Courier", 20))
		data = self.tkw.setData(" ",padx=(5, 2), pady=5, sticky=W)
		self.tkw.insert(Entry, 0, data)
		self.tkw.set("width", 2)
		#
		# 0 4
		data = self.tkw.setData(text=":", pady=5, sticky=W)
		self.tkw.insert(Label, 0, data)
		#
		# 0 5
		data = self.tkw.setData(" ",padx=(2, 5), pady=5, sticky=W)
		self.tkw.insert(Entry, 0, data)
		self.tkw.set("width", 2)
		#
		# 0 6
		data = self.tkw.setData(text="+", pady=5, sticky=W)
		self.tkw.insert(Label, 0, data)
		#
		# 0 7
		data = self.tkw.setData(" ",padx=(5, 2), pady=5, sticky=W)
		self.tkw.insert(Entry, 0, data)
		self.tkw.set("width", 2)
		#

		self.poluvremeVar = StringVar()
		self.poluvremeVar.set(self.defaultVar)
		self.stringVars.append(self.poluvremeVar)

		# 0 8
		self.tkw.set_font(("Courier", 15))
		data = self.tkw.setData(text="Prvo poluvreme", sticky=W)
		self.tkw.insert(Radiobutton, 0, data)
		self.tkw.set("value", "prvo")
		self.tkw.set("variable", self.stringVars[-1])
		self.tkw.set("command", lambda var=self.stringVars[-1]: self.getPoluvreme(var))

		# 0 9
		data = self.tkw.setData(text="Drugo poluvreme", sticky=W)
		self.tkw.insert(Radiobutton, 0, data)
		self.tkw.set("value", "drugo")
		self.tkw.set("variable", self.stringVars[-1])
		self.tkw.set("command", lambda var=self.stringVars[-1]: self.getPoluvreme(var))


		# 0 10
		self.tkw.set_font(("Courier", 20))
		data = self.tkw.setData("Obrisi", sticky=W)
		self.tkw.insert(Button,0,data)
		zaLambdu = lambda var1=self.getLastRadioBtn(),var2=self.stringVars.index(self.stringVars[-1]): self.deleteRow(var1, var2)
		self.tkw.set("command", zaLambdu)

		self.update()
		self.canvas.yview_moveto(2)
		self.update()

	def getLista(self):
		return self.frame.winfo_children()[:-12:-1]

	def clickOnTab(self):
		lista = self.getLista()
		brojac = 0
		radioBtns = []
		for i in lista:
			if str(type(i)) == "<class 'tkinter.Entry'>":
				if len(i.get()) > 0:
					brojac += 1
			elif str(type(i)) == "<class 'tkinter.Radiobutton'>":
				radioBtns.append(i)

		lastRadio = -1
		if brojac == 3:
			while True:
				try:
					vrednost = self.stringVars[lastRadio].get()
					self.defaultVar = vrednost
					self.addRow()
					startFocus(self)

					break
				except:
					lastRadio -= 1
					continue

	def getAllElements(self):
		return self.frame.winfo_children()

	def getPoluvreme(self, var):
		return var.get()

	def removeCharFromEntry(self, slovo):
		lista = self.getAllElements()
		for i in lista:
			if str(type(i)) == "<class 'tkinter.Entry'>":
				value = i.get()
				value2 = re.sub("[a-zA-Z]", "", value)
				try:
					int(value2)
				except:
					value2 = ""

				i.delete(0, END)
				i.insert(0, value2)

	def deleteRow(self, lastRadioBtn, stringVarIndex):
		lastRadioBtnIndex = self.getAllElements().index(lastRadioBtn)
		startIndex = lastRadioBtnIndex - 7
		deleteBtnIndex = startIndex + 8

		templista = self.getAllElements()
		for i in range(startIndex, deleteBtnIndex + 1):
			templista[i].destroy()
		self.stringVars[stringVarIndex] = None

	def getLastRadioBtn(self):
		lastRadioBtn = self.getAllElements()[-2]
		return lastRadioBtn

	def setAudio(self, par):
		self.footballEditor.audioVar = par

	def setExt(self, par):
		if par == "":
			self.footballEditor.extt = self.footballEditor.originalExt
		elif par != "":
			self.footballEditor.extt = par

	def goBack(self):
		self.controller.prebaci_frejm("FootballFrame")

	def saveToFile(self):

		if self.controller.page_name == "HighlightsFrame":
			saveToFile(self)

	def removeAllEntries(self):

		removeAllEntries(self)

	def checkFileEntries(self):
		if self.controller.page_name == "HighlightsFrame":
			highlightsPutanja = ""
			extt = ""
			try:
				if str(type(fileDialog)) == "<class 'module'>":
					rep = fileDialog.askopenfilename(
						parent=self.frame,
						initialdir='/adffgdfg',
						initialfile='tmp',
						filetypes=[
							("All files", "*")])
					highlightsPutanja = rep
					extt = os.path.splitext(str(highlightsPutanja))[1]
			except Exception as e:
				print("greska: " + str(e))

			if highlightsPutanja != "" and extt == ".txt":

				checkingPretraga(self,messagebox,highlightsPutanja)

			else:
				messagebox.showinfo('Highlights load', 'txt fajl format je neophodan.')

	def closeApp(self):
		self.saveToFile()
		self.controller.quit()

	def setFirstReg(self):
		if self.controller.page_name == "FootballFrame":
			promeniTextZaMecLabel(self, "FIRST HALF", "firstRegular", "normal", "disabled")
			self.controller.prozori["FootballFrame"].showOrHideFrameForCut(True)

	def setSecondtReg(self):
		if self.controller.page_name == "FootballFrame":
			promeniTextZaMecLabel(self, "SECOND HALF", "secondRegular", "disabled", "normal")
			self.controller.prozori["FootballFrame"].showOrHideFrameForCut(True)

	def setFullReg(self):
		if self.controller.page_name == "FootballFrame":
			promeniTextZaMecLabel(self, "MEC", "regularFull", "normal", "normal")
			self.controller.prozori["FootballFrame"].showOrHideFrameForCut(False)
