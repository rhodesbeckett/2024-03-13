from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import os.path
import re
import subprocess


# prvi str je source drugi je naziv iscek
class FootballEditor(object):
	putanja = ""
	extt = ""
	vremenaUSekundama = []
	highlightsCounter = 0
	prvo_pol = 0
	drugo_pol = 0
	prvo_pol_extra = 0
	drugo_pol_extra = 0
	sablon1 = "(\d{1,3}):(\d{1,3})"
	sablon2 = re.compile(sablon1 + "\s" + sablon1)
	sablon3 = re.compile(sablon1 + "\s(\d{1,3})")
	sablon4 = re.compile(r'' + sablon1)
	ceoMecSekunde = 0
	tested = False
	imeFoldera = ""


	# sablonZaHighlights = re.compile("(\d{1,2}):(\d{1,2}) (\d{1,2}|\n")

	def getPutanja(self, fileDialog, frame, putanja=""):
		try:
			if (str(type(fileDialog)) == "<class 'module'>"):
				rep = fileDialog.askopenfilename(
					title="Load file",
					parent=frame,
					initialdir='/adffgdfg',
					initialfile='tmp',
					filetypes=[
						("All files", "*")])
				self.putanja = rep
				self.extt = os.path.splitext(str(self.putanja))[1]
		except Exception as e:
			print("greska: " + str(e))

	def seckanje(self, br, pocetak, kraj):
		self.napraviFolder()
		naziv = self.imeFoldera+"/video" + str(br) + self.extt
		ffmpeg_extract_subclip(self.putanja, pocetak, kraj, targetname=naziv)

	def canRun(self):
		if (len(self.vremenaUSekundama) == self.highlightsCounter and self.tested == True):
			#  and self.checkVremenaUSekundama()
			return True
		else:
			return False
	def checkVremenaUSekundama(self):
		if(self.ceoMecSekunde == 0):
			return None
		for i in range(len(self.vremenaUSekundama)):
			if(self.vremenaUSekundama[i][0]>self.ceoMecSekunde or self.vremenaUSekundama[i][1]>self.ceoMecSekunde):
				print("minut:")
				print(self.vremenaUSekundama[i][0])
				print("sekunde:")
				print(self.vremenaUSekundama[i][1])

				print("ceo mec sekunde:")
				print(self.ceoMecSekunde)

				return False
		return True
	def napraviFolder(self):
		self.imeFoldera = self.putanja.split("/")[-1].split(".")[0].replace(" ","")
		if(not os.path.exists(self.imeFoldera)):
			os.mkdir(self.imeFoldera)
		# else:
		# 	shutil.rmtree(self.imeFoldera)
		# 	os.mkdir(self.imeFoldera)

	def mergeAll(self):
		# matchDir = os.listdir(self.imeFoldera)
		matchDir = self.orderOfVids()
		imetxtFajl = str(self.imeFoldera+"\\"+"mylist.txt")
		txtFajl = open(imetxtFajl,"w")
		for i in range(len(matchDir)):
			if(matchDir[i].endswith("txt")):
				continue
			elif (matchDir[i].endswith("output.mkv")):
				continue
			imeFajla = matchDir[i]
			line = "file '{}\{}'\n".format(self.imeFoldera,imeFajla)
			txtFajl.write(str(line))
		txtFajl.close()

		outputName = self.imeFoldera+"\\output"+self.extt
		if(os.path.exists(outputName)):
			os.unlink(outputName)
		command = str("ffmpeg -f concat -safe 0 -i {} -c copy {}/{}{}".format(imetxtFajl,self.imeFoldera,"output",self.extt))
		print(command)
		subprocess.call(command,shell=True)
	def orderOfVids(self):
		duzinaListe = len(self.vremenaUSekundama)
		novaLista = []
		for i in range(0,duzinaListe):
			novaLista.append("video"+str(i)+self.extt)
		return novaLista





