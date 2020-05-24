from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import os.path
import re
from editor.TimeConverter import *
from editor.Checker import *


# prvi str je source drugi je naziv iscek
class FootballEditor(object):
	putanja = ""
	extt = ""
	prvo_pol = ""
	drugo_pol = ""
	sablon1 = "(\d{1,3}):(\d{1,3})"
	sablon2 = re.compile(sablon1 + "\s" + sablon1)
	sablon3 = re.compile(sablon1 + "\s(\d{1,3})")
	sablon4 = re.compile(r'' + sablon1)

	def __init__(self):
		self.checker = Checker()
		self.timeConverter = TimeConverter()

	# sablonZaHighlights = re.compile("(\d{1,2}):(\d{1,2}) (\d{1,2}|\n")

	def getPutanja(self, fileDialog, frame, putanja=""):
		try:
			if (str(type(fileDialog)) == "<class 'module'>"):
				rep = fileDialog.askopenfilename(
					parent=frame,
					initialdir='/',
					initialfile='tmp',
					filetypes=[
						("All files", "*")])
				self.putanja = rep
				self.extt = os.path.splitext(str(self.putanja))[1]
				print(self.extt)
		except Exception as e:
			print("greska: " + str(e))

	def setPrvoPol(self, prvoPol):
		pretraga = self.sablon4.findall(prvoPol)
		poluvreme = self.timeConverter.setVreme(pretraga)
		if (len(poluvreme.keys()) == 3):
			poluvreme = "{}:{}:{},00".format(poluvreme["sat"],poluvreme["minut"], poluvreme["sekunda"])
			self.prvo_pol = int(self.timeConverter.konvert_u_sekunde(poluvreme))
			print(self.prvo_pol)
			return self.prvo_pol
			# print(self.prvo_pol)
		else:
			print("greska u set prvo pol")

	def setDrugoPol(self, drugoPol):
		pretraga = self.sablon4.findall(drugoPol)
		poluvreme = self.timeConverter.setVreme(pretraga)
		if (len(poluvreme.keys()) == 3):
			poluvreme = "{}:{}:{},00".format(poluvreme["sat"],poluvreme["minut"], poluvreme["sekunda"])
			self.drugo_pol = int(self.timeConverter.konvert_u_sekunde(poluvreme))
			print(self.drugo_pol)
			return self.drugo_pol
			# print(self.drugo_pol)
		else:
			print("greska u set drugo pol")

	def provera_fajla(self, fajl):
		video = self.checker.provera_fajla(fajl, self.sablon2, self.sablon3,
										   self.prvo_pol, self.drugo_pol)
		print(self.putanja)
		if (str(type(video)) == "<class 'list'>"):
			for i in range(len(video)):
				pocetak = video[i][0]
				kraj = video[i][1]
				self.seckanje(i, pocetak, kraj)

		else:
			print("greska")

	def seckanje(self, br, pocetak, kraj):
		naziv = "video" + str(br) + self.extt
		ffmpeg_extract_subclip(self.putanja, pocetak, kraj, targetname=naziv)
