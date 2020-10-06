def startTCut(obj,threading):
	obj.t_cut = threading.Thread(target=lambda var=True: obj.runCut(var))
	obj.t_cut.start()

def checkIfReady(obj,provera,messagebox):
	checkVar = False
	if (provera == True):
		if (obj.footballEditor.canRun()):
			if (obj.footballEditor.getCurrentPutanja() != ""):
				vremenaUSekundamaProvera = obj.footballEditor.checkVremenaUSekundama()
				if (vremenaUSekundamaProvera):
					checkVar = True

				elif (vremenaUSekundamaProvera == False):
					messagebox.showinfo('Renderovanje', 'Ispravite highlights.')
					checkVar = False

				elif (vremenaUSekundamaProvera == None):
					messagebox.showinfo('Renderovanje', 'Testirajte mec.')
					checkVar = False
			else:
				messagebox.showinfo('Renderovanje', 'Niste dodali fajl.')
				checkVar = False
		else:
			messagebox.showinfo('Renderovanje', 'Program i dalje nije spreman za render.')
			checkVar = False
	elif(provera == False):
		return True
	return checkVar


def runCut(obj, messagebox,provera):
	checkVar = checkIfReady(obj,provera,messagebox)
	# ako je tacna provera onda moze cut da pocne
	if (checkVar == True):
		forRun2 = True
		if (obj.footballEditor.tipHighlightsa in ("firstRegular", "secondRegular")):
			lokacijaVideaa = obj.getVideoLocation()
			# ako je prazno onda reci da je greska u pitanju
			if (lokacijaVideaa == "" or lokacijaVideaa == None):
				messagebox.showinfo('Renderovanje', 'Niste naveli ime foldera.')
				forRun2 = False
			elif (lokacijaVideaa != "" or lokacijaVideaa != None):
				obj.footballEditor.napraviFolder(lokacijaVideaa)
				forRun2 = True
		else:
			obj.footballEditor.napraviFolder("")
			forRun2 = True

		if (forRun2 == True):

			iCounter = obj.footballEditor.getInfoAboutVideos("len")
			video = obj.footballEditor.vremenaUSekundama
			for i in range(len(video)):
				pocetak = video[i][0]
				kraj = video[i][1]
				seckanje = obj.footballEditor.seckanje(iCounter, pocetak, kraj)
				# ovde None znaci da klip
				# nije ranije postojao
				# i da je kreiran
				if (seckanje == None):
					iCounter += 1
			if (provera == True):
				messagebox.showinfo('Cut', 'Cut je uspesno zavrsen.')

