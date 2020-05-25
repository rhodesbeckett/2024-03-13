from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import os.path
import re


# prvi str je source drugi je naziv iscek
class FootballEditor(object):
	putanja = ""
	extt = ""
	vremenaUSekundama = []
	highlightsCounter = 0
	prvo_pol = 0
	drugo_pol = 0
	sablon1 = "(\d{1,3}):(\d{1,3})"
	sablon2 = re.compile(sablon1 + "\s" + sablon1)
	sablon3 = re.compile(sablon1 + "\s(\d{1,3})")
	sablon4 = re.compile(r'' + sablon1)
	tested = False


	def __init__(self):
		print("open")

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

	def seckanje(self, br, pocetak, kraj):
		naziv = "video" + str(br) + self.extt
		ffmpeg_extract_subclip(self.putanja, pocetak, kraj, targetname=naziv)

	def canRun(self):
		if (len(self.vremenaUSekundama) == self.highlightsCounter and self.tested == True):
			return True
		else:
			return False
