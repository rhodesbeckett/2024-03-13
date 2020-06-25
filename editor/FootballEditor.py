from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import os.path
import re
import subprocess
from moviepy.video.io.VideoFileClip import VideoFileClip


# prvi str je source drugi je naziv iscek
class FootballEditor(object):
	putanja = ""
	prvoPolPutanja = ""
	drugoPolPutanja = ""
	extt = ""
	originalExt = ""
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
	tipHighlightsa = ""
	audioVar = True


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
				if (self.tipHighlightsa=="firstRegular"):
					self.prvoPolPutanja = rep
					self.extt = os.path.splitext(str(self.prvoPolPutanja))[1]
					self.originalExt = self.extt
					self.drugoPolPutanja = ""
					self.putanja = ""
				elif (self.tipHighlightsa == "secondRegular"):
					self.drugoPolPutanja = rep
					self.extt = os.path.splitext(str(self.drugoPolPutanja))[1]
					self.originalExt = self.extt
					self.prvoPolPutanja = ""
					self.putanja = ""
				elif (self.tipHighlightsa == "regularFull"):
					self.putanja = rep
					self.extt = os.path.splitext(str(self.putanja))[1]
					self.originalExt = self.extt
					self.prvoPolPutanja = ""
					self.drugoPolPutanja = ""
		except Exception as e:
			print("greska: " + str(e))

	def seckanje(self, br, pocetak, kraj):
		drugiDeo = "_" + str(pocetak) + str(kraj) + self.extt
		naziv = self.imeFoldera+"/video" + str(br) + drugiDeo
		print(naziv)
		#fajl ne postoji dakle moze da se secka
		if(self.checkForFile(drugiDeo) == False):
			fajl = VideoFileClip(self.getCurrentPutanja())
			new = fajl.subclip(pocetak, kraj)
			if(self.extt == ".mp4"):
				new.write_videofile(naziv,logger=None,audio= self.audioVar)
			else:
				ffmpeg_extract_subclip(self.getCurrentPutanja(), pocetak, kraj, targetname=naziv)
		else:
			return True

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
	def napraviFolder(self,par1):
		if(par1 == ""):

			self.imeFoldera = self.putanja.split("/")[-1].split(".")[0].replace(" ","")
			if(not os.path.exists(self.imeFoldera)):
				os.mkdir(self.imeFoldera)
		else:
			self.imeFoldera = par1
			if (not os.path.exists(self.imeFoldera)):
				os.mkdir(self.imeFoldera)
		# else:
		# 	shutil.rmtree(self.imeFoldera)
		# 	os.mkdir(self.imeFoldera)

	def mergeAll(self):
		# matchDir = os.listdir(self.imeFoldera)
		# matchDir = self.orderOfVids()
		matchDir = self.getInfoAboutVideos("list2")[:]
		listWithNumbers = self.getInfoAboutVideos("list")[:]

		imetxtFajl = str(self.imeFoldera+"\\"+"mylist.txt")
		txtFajl = open(imetxtFajl,"w")

		for i in range(len(listWithNumbers)):
			pocetak = "video"+str(i)+"_"
			imeFajla = self.findNameOfVideo(matchDir,pocetak)
			if(imeFajla!= None):
				line = "file '{}\{}'\n".format(self.imeFoldera, imeFajla)
				txtFajl.write(str(line))

		txtFajl.close()
		# outputName = self.imeFoldera+"\\output"+self.extt
		outputName = self.imeFoldera + "\\output" +self.extt
		if(os.path.exists(outputName)):
			os.unlink(outputName)

		command = str("ffmpeg -f concat -safe 0 -i {} -c copy {}/{}{}".format(imetxtFajl,self.imeFoldera,"output",".mp4"))
		print(command)
		subprocess.call(command,shell=True)

	def orderOfVids(self):
		duzinaListe = len(self.vremenaUSekundama)
		novaLista = []
		for i in range(0,duzinaListe):
			novaLista.append("video"+str(i)+self.extt)
		return novaLista
	def findNameOfVideo(self,lista,var):
		#var je pocinje sa
		for i in lista:
			if(i.startswith(var)):
				return i

	def getCurrentPutanja(self):
		lista = [self.putanja,self.prvoPolPutanja,self.drugoPolPutanja]
		putanja = ""
		for i in lista:
			if(i!=""):
				putanja = i
				break
		return putanja

	def getInfoAboutVideos(self,info):
		sablon = re.compile(r'video(\d{1,})')
		putanja = self.imeFoldera
		fajlovi = os.listdir(putanja)
		videos2 = []
		videosForList2 = []
		for i in range(len(fajlovi)):
			if(fajlovi[i].startswith("video")):
				pretraga = sablon.findall(fajlovi[i])
				if(len(pretraga)>0):
					videos2.append(int(pretraga[0]))
				videosForList2.append(fajlovi[i])
		# sortirana lista sa brojevima
		videos2.sort()
		# sortirana lista sa nazivima(nije bitan redosled)
		videosForList2.sort()
		if(info=="len"):
			if(len(videos2)>0):
				return videos2[-1]+1
			else:
				return 0
		elif(info=="list"):
			return videos2
		elif(info=="list2"):
			return videosForList2
	def checkForFile(self,strr):
		lista = self.getInfoAboutVideos("list2")[:]
		for i in lista:
			if (i.endswith(strr)):
				return True
		return False






