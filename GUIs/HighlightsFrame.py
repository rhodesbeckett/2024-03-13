from tkinter import *
from editor import FootballEditor


class HighlightsFrame(Frame):
	def __init__(self, parent, controller,fe,checker):
		Frame.__init__(self, parent)
		self.footballEditor = fe
		self.checker = checker
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

		Label(self.frame, text="Kraj", font=("Courier", 20)).grid(row=self.rowH, column=self.columnH, padx=(0, 0),
																  pady=5, sticky=W)
		self.columnH += 1

		self.entryDrugoPolMin = Entry(self.frame, width=2, font=("Courier", 20))
		self.entryDrugoPolMin.grid(row=self.rowH, column=self.columnH, padx=(5, 2), pady=5, sticky=W)
		self.columnH += 1

		Label(self.frame, text=":", font=("Courier", 20)).grid(row=self.rowH, column=self.columnH, padx=(0, 0), pady=5,
															   sticky=W)
		self.columnH += 1

		self.entryDrugoPolSec = Entry(self.frame, width=2, font=("Courier", 20))
		self.entryDrugoPolSec.grid(row=self.rowH, column=self.columnH, padx=(2, 5), pady=5, sticky=W)
		self.columnH += 1

		self.poluvremeVar = StringVar()
		self.poluvremeVar.set(self.defaultVar)
		self.stringVars.append(self.poluvremeVar)

		Radiobutton(self.frame, text='Prvo poluvreme', font=("Courier", 20),value='prvo', variable=self.stringVars[-1], command=lambda var=self.stringVars[-1]: self.getPoluvreme(var)).grid(
			row=self.rowH, column=self.columnH, sticky=W
		)
		self.columnH += 1
		Radiobutton(self.frame, text='Drugo poluvreme', font=("Courier", 20), value='drugo', variable=self.stringVars[-1], command=lambda var=self.stringVars[-1]: self.getPoluvreme(var)).grid(
			row=self.rowH, column=self.columnH, sticky=W
		)
		self.columnH = 0

	def getLista(self):
		return self.frame.winfo_children()[:-11:-1]

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

		if (brojac == 4):
			vrednost = self.stringVars[-1].get()
			self.defaultVar = vrednost
			self.addRow()
			self.getLista()[-2].focus()


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
				if(value.endswith(slovo.lower())):
					value = value.replace(slovo.lower(), "")
				elif(value.endswith(slovo.upper())):
					value = value.replace(slovo.upper(),"")
				i.delete(0,END)
				i.insert(0, value)
				print("VALUE REMOVE "+i.get())


