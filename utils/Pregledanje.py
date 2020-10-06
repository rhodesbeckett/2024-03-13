import threading, random, re


def startFocus(obj):
	obj.t_render = threading.Thread(target=obj.getLista()[7].focus)
	obj.t_render.start()


# DOBIJANJE POLUVREMENA IZ DUGMETA
def getPoluvremeFromRButton(obj, lista, rbtnIndex, tip):
	varIndex = str(lista[rbtnIndex]).split(".!")[5].split("radiobutton")[1]
	varIndex = int((int(varIndex) / 2) - 1)
	if (tip == "objekat"):
		return obj.stringVars[varIndex].get()
	else:
		return varIndex


# DOBIJANJE PODATAKA IZ JEDNOG REDA
def getRowData(obj, row, templista, i):
	rbtnIndex = templista.index(i) + 2
	poluvreme = getPoluvremeFromRButton(obj, templista, rbtnIndex, "objekat")
	minut = row[0].get()
	sekunda = row[1].get()
	end = row[2].get()

	if (minut == ""):
		minut = "0"
	if (sekunda == ""):
		sekunda = "0"
	if (end == ""):
		end = "0"
	row = {"minut": minut, "sekunda": sekunda, "end": end, "poluvreme": poluvreme}
	return row


# DODAVANJE STRINGA U FAJL
def setForFile(row):
	rowFile = row["minut"] + " " + row["sekunda"] + " " + row["end"] + " " + row["poluvreme"] + "\n"
	return rowFile


# OTVARANJE FAJLA ZA CUVANJE PREGLEDA
def otvaranjeFajla(obj):
	if (obj.imeTxtFajla == ""):
		obj.imeTxtFajla = "highlights" + str(random.randint(1, 1000)) + ".txt"
		fajl = open(obj.imeTxtFajla, "w", encoding="utf-8")
	else:
		fajl = open(obj.imeTxtFajla, "w", encoding="utf-8")
	return fajl

def initDataForReading():
	return -1, 0, []

def getPoluvremeFromRed(redovi, i):
	return redovi[i][3]

def modifyEntries(entries, redovi, red):
	entries[2].insert(0, redovi[red][0])
	entries[1].insert(0, redovi[red][1])
	entries[0].insert(0, redovi[red][2])
	if (len(str(redovi[red][0])) == 3):
		entries[2]["width"] = 3

# DODAVANJE REDOVA U H..FRAME
def addingToEntries(obj, redovi):
	obj.removeAllEntries()
	red, brojac, entries = initDataForReading()
	brojacForStringVars = 0
	for i in range(len(redovi)):
		obj.defaultVar = getPoluvremeFromRed(redovi, i)
		# if (brojacForStringVars == 0):
		# 	self.stringVars = []
		# 	brojacForStringVars + 1
		obj.addRow()

		lista = obj.getLista()

		for j in range(len(lista)):
			if (str(type(lista[j])) == "<class 'tkinter.Entry'>"):

				brojac += 1
				entries.append(lista[j])
				if (brojac == 3):
					red += 1
					modifyEntries(entries, redovi, red)

					setStringVars(obj, lista, redovi, red)

					entries = []
					brojac = 0

def addToRedovi(pretraga, redovi):
	forEntries = pretraga[0][0].split(" ")
	redovi.append([forEntries[0], forEntries[1], forEntries[2], forEntries[3].split("\n")[0]])

def otvaranjeFajla2(highlightsPutanja):
	sablon = re.compile(r'(.*\s.*\s.*(\sprvo|drugo|))')
	fajl = open(highlightsPutanja, "r", encoding="utf-8")
	return sablon, fajl, []

# PROVERA PRETRAGE IZ FAJLA ZA CITANJE HIGHLIGHTS-A
def checkingPretraga(obj, messagebox, highlightsPutanja):
	sablon, fajl, redovi = otvaranjeFajla2(highlightsPutanja)

	linija = fajl.readline()

	pretraga = sablon.findall(linija)
	while (linija != ""):
		pretraga = sablon.findall(linija)
		if (len(pretraga) > 0):
			if (len(pretraga[0]) > 0):
				addToRedovi(pretraga, redovi)
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
	if (not pretraga == []):
		addingToEntries(obj, redovi)

	else:
		messagebox.showinfo('Highlights load',
							'Ispravite greske u highlights txt da bi ste uspesno ucitali.')

# CTRL+S ILI CUVANJE PREGLEDA U FAJL
def saveToFile(obj):
	fajl = otvaranjeFajla(obj)

	templista = obj.getAllElements()[:]
	brojac = 0
	row = []
	for i in templista:
		if (str(type(i)) == "<class 'tkinter.Entry'>"):
			brojac += 1
			row.append(i)
			if (brojac == 3):
				getRowData(obj, row, templista, i)
				rowFile = setForFile(getRowData(obj, row, templista, i))
				fajl.write(rowFile)
				brojac = 0
				row = []
	fajl.close()


# ---

# UKLANJANJE SVIH UNOSA U HIGHLIGHTS
def removeAllEntries(obj):
	lista = obj.getAllElements()

	exceptions = [".!frame.!highlightsframe.!canvas.!frame.!menu",
				  ".!frame.!highlightsframe.!canvas.!frame.!button"]
	for i in lista:
		if (str(i) not in exceptions):
			i.destroy()
	for b in range(len(obj.stringVars)):
		obj.stringVars[b] = None

def setStringVars(obj, lista, redovi, red):
	rBtn = lista[1]
	varIndex = getPoluvremeFromRButton(obj, lista, lista.index(rBtn), "indeks")
	obj.stringVars[varIndex].set(redovi[red][3].split("\n")[0])

# def checkHighlights(self,list,stringVars):



def proveraTipa(self, tip):
	if (self.footballEditor.tipHighlightsa == tip):
		return True
	return False

def getToContinue(poluvreme,stringVars):
	for i in range(len(stringVars)):
		if (stringVars[i] != None):
			if (stringVars[i].get() != poluvreme):
				toContinue = False
				return False
	return True

def daLiJeEntry(widget):
	if (str(type(widget)) == "<class 'tkinter.Entry'>"):
		return True
	return False

def proveraKolone(self,timeStamp,sta,forAdd):
	sekunde = self.sekundeObj.convertToSeconds(timeStamp.get(), sta)
	if (sekunde == None):
		timeStamp["bg"] = "#ff6529"
		return sekunde,False
	else:
		timeStamp["bg"] = "#ffffff"
		return sekunde,forAdd

def isPoluvreme12NotNula(obj):
	if (not obj.footballEditor.prvo_pol == 0 or not obj.footballEditor.drugo_pol == 0):
		return True
	return False

def paint(timeStamp):
	for i in range(len(timeStamp)):
		timeStamp[i]["bg"] = "#ffffff"

def calculate(obj,pocetakMin,pocetakSek,krajSekunde,timeStamp,poluvreme):
	if (poluvreme == "prvo"):
		pocetak = obj.footballEditor.prvo_pol + (pocetakMin + pocetakSek)
	else:
		pocetak = obj.footballEditor.drugo_pol + (pocetakMin + pocetakSek) - 2700

	kraj = pocetak + krajSekunde
	del timeStamp
	timeStamp = []

def calculatePocetak(obj,pocetakMin,pocetakSek,poluvreme):
	if(poluvreme == "prvo"):
		return obj.footballEditor.prvo_pol + (pocetakMin + pocetakSek)
	else:
		return obj.footballEditor.drugo_pol + (pocetakMin + pocetakSek) - 2700

def hidePoluvreme(poluvreme,firstFrame,secondFrame):
	show = []
	hide = []
	show2 = []
	hide2 = []
	if(poluvreme == "prvo"):
		show =[3,4]
		hide=[5,6]
		hide2 = [3,4,5]
	elif(poluvreme == "drugo"):
		show = [5,6]
		hide = [3,4]
		hide2 = [3,4,5]
	else:
		show = [3,4,5,6]
		show2 = [3,4,5]

	for i in range(len(firstFrame)):
		if (i in show):
			firstFrame[i].grid()
		elif (i in hide):
			firstFrame[i].grid_remove()

	for i2 in range(len(secondFrame)):

		if (i2 in show2):
			secondFrame[i2].grid()
		elif (i2 in hide2):
			secondFrame[i2].grid_remove()


def calculateKraj(pocetak,krajSekunde):
	return pocetak + krajSekunde

def setLabel(obj,metoda,poruka,tested):
	obj.tkw.set("text", poruka, 0, 12)
	obj.footballEditor.tested = tested
	if(poruka.endswith("BUT")):
		obj.tkw.get_object(0, 12).bind("<Button-1>", lambda e: metoda("FootballFrame"))
	elif(poruka.endswith("NOT OK")):
		obj.tkw.get_object(0, 12).bind("<Button-1>", lambda e: metoda("HighlightsFrame"))
	else:
		obj.tkw.get_object(0, 12).bind("<Button-1>", lambda e: metoda())

def promeniTextZaMecLabel(obj, text, tip,prvo,drugo):
	obj.controller.prozori["FootballFrame"].tkw.set("text", text, 0, 0)
	obj.controller.prozori["FootballFrame"].footballEditor.tipHighlightsa = tip
	#ovde je normal pa disabled
	for i in [1,3]:
		obj.controller.prozori["FootballFrame"].tkw.set("state", prvo, 1, i)
	for i2 in [5,7]:
		obj.controller.prozori["FootballFrame"].tkw.set("state", drugo, 1, i2)