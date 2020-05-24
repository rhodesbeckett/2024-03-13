from editor.TimeConverter import *
from tkinter import Entry


class Checker(object):
	sablon = ""
	tc = TimeConverter()
	vremenaUSekundama = []

	def provera_fajla(self, fajl, sablon2, sablon3, prvoPol, drugoPol):
		# E:\Projekat2\projekat2-nrs\highlights.txt
		fajl = open(fajl)
		print("TU smo")
		linija = fajl.readline()
		vremena_u_sekundama = []
		poluvreme = 0
		while (linija != ""):
			if (linija == "11\n"):
				poluvreme = 1
			elif (linija == "22\n"):
				poluvreme = 2
			pretraga = sablon2.findall(linija)
			print(pretraga)
			if (len(pretraga) > 0):
				if (len(pretraga[0]) == 4):
					# print(pretraga[0][0:2])
					pocetak = self.tc.setVreme((pretraga[0][0:2],))
					kraj = self.tc.setVreme((pretraga[0][2:4],))
					if (poluvreme == 1):
						pocetak = prvoPol + self.getSekunde(pocetak)
						kraj = prvoPol + self.getSekunde(kraj)
					elif (poluvreme == 2):
						pocetak = drugoPol + self.getSekunde(pocetak)
						kraj = drugoPol + self.getSekunde(kraj)
					vremena_u_sekundama.append((pocetak, kraj))

			elif (len(pretraga) == 0):
				if (linija != "11\n" or linija != "22\n"):
					pretraga3 = sablon3.findall(linija)
					pocetak = self.tc.setVreme(pretraga3)

		linija = fajl.readline()
		fajl.close()
		return vremena_u_sekundama


	def provera_putanje(self):
		print("ok")


	def provera_prvog_pol(self, fajl):
		print("ok")


	def provera_drugog_pol(self):
		print("ok")


	def getSekunde(self, podatak):

		if (len(podatak.keys()) == 3):
			podatak2 = "{}:{}:{},00".format(podatak["sat"],podatak["minut"], podatak["sekunda"])
			podatak2 = int(self.tc.konvert_u_sekunde(podatak2))
			return podatak2


	def proveraEntries(self, lista = [],stringVars = [],prvoPol = 0,drugoPol = 0):
		vremena_u_sekundama = []
		timeStamps = []
		timeStamp = []
		brojac = 0
		for i in lista:

			if (str(type(i)) == "<class 'tkinter.Entry'>"):
				if (brojac < 4):
					brojac += 1
					timeStamp.append(i)
					if (brojac == 4):
						brojac = 0

						minut1 = timeStamp[0].get()
						sekunda1 = timeStamp[1].get()
						minut2 = timeStamp[2].get()
						sekunda2 = timeStamp[3].get()


						pocetak = self.tc.setVreme(((minut1, sekunda1),))
						kraj = self.tc.setVreme(((minut2, sekunda2),))

						rbtnIndex = lista.index(i)+2
						varIndex = str(lista[rbtnIndex]).split(".!")[5].split("radiobutton")[1]
						varIndex = int((int(varIndex)/2)-1)
						poluvreme = stringVars[varIndex].get()

						if (poluvreme == "prvo"):

							pocetak = prvoPol + self.getSekunde(pocetak)
							try:
								kraj = prvoPol + self.getSekunde(kraj)
							except:
								print("greska")

						elif (poluvreme == "drugo"):
							pocetak = drugoPol + self.getSekunde(pocetak)
							kraj = drugoPol + self.getSekunde(kraj)
						vremena_u_sekundama.append((pocetak, kraj))

						timeStamp = []
		self.vremenaUSekundama = vremena_u_sekundama
		return vremena_u_sekundama
	def setEntry(self,entry,minut=False,sekunda=False):
		entryData = entry.get()
		if(str(entryData).isdigit()):
			if(len(entryData)>0 and len(entryData)<3):
				if(len(entryData)==2):
					if(minut==True):
						if(int(entryData)<100):
							print("minut")
					elif(sekunda==True):
						if(int(entryData)<60):
							print("sekunda")




