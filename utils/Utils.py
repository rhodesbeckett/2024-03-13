def getStyles(obj, W, E):
	recnik = {}

	# treca kolona sadrzi novi frame za dodavanje poluvremena



	# ovo je nov red koji sadrzi



	# ovaj recnik se nalazi na trecoj koloni poseban frame
	# recnik.setdefault(obj.justCut,
	# 				  {"text": "JUST CUT", "row": 0, "column": 0, "padx": 1, "pady": 5, "sticky": W})
	#
	# recnik.setdefault(obj.labelFolder,
	# 				  {"text": "FOLDER", "row": 0, "column": 1, "padx": 15, "pady": 5, "sticky": E})
	#
	#
	# recnik.setdefault(obj.entryVideosLocation,
	# 				  {"text": "", "row": 0, "column": 2, "padx": (5, 2), "pady": 5, "sticky": E})


	return recnik


def setWidgets(objs):
	for obj in objs:
		obj["font"] = ("Courier", 15)
		if (objs[obj]["text"] != ""):
			obj["text"] = objs[obj]["text"]
		row = objs[obj]["row"]
		column = objs[obj]["column"]
		padx = objs[obj]["padx"]
		pady = objs[obj]["pady"]
		sticky = objs[obj]["sticky"]
		obj.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)


def keyPress(obj, event):
	if (event.char == "\t"):
		if (obj.page_name == "HighlightsFrame"):
			obj.prozori["HighlightsFrame"].clickOnTab()
	elif (event.char == "g" or event.char == "G"):
		obj.prebaci_frejm("FootballFrame")
		obj.prozori["HighlightsFrame"].removeCharFromEntry(event.char)
	elif (event.char == "f" or event.char == "F"):
		if (obj.page_name == "HighlightsFrame"):
			obj.prozori["HighlightsFrame"].addRow()
			obj.prozori["HighlightsFrame"].removeCharFromEntry(event.char)
	elif (event.char == '\x13'):
		obj.prozori["HighlightsFrame"].saveToFile()


def setLabelPoluvreme(frame, label, minut, sekunda, poluvreme):
	if (minut != None and sekunda != None):
		label["text"] = "OK"
		label.bind("<Button-1>", lambda e: frame.doNothing())
		if (poluvreme == 1):
			frame.footballEditor.setPrvoPoluvreme(minut + sekunda)
		else:
			frame.footballEditor.setDrugoPoluvreme(minut + sekunda)

	else:
		label["text"] = "NOT OK"
		label.bind("<Button-1>", lambda e: frame.controller.prebaci_frejm("FootballFrame"))
		if (poluvreme == 1):
			frame.footballEditor.setPrvoPoluvreme(0)
		else:
			frame.footballEditor.setDrugoPoluvreme(0)
