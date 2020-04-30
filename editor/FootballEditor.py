
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
    sablon1 = "(\d{1,2}):(\d{1,2})"
    sablon2 = re.compile(sablon1+"\s"+sablon1)
    sablon3 = re.compile(sablon1+"\s(\d{1,2})")
    sablon4 = re.compile(r''+sablon1)

    def __init__(self):
        self.checker = Checker()
        self.timeConverter = TimeConverter()

    # sablonZaHighlights = re.compile("(\d{1,2}):(\d{1,2}) (\d{1,2}|\n")

    def getPutanja(self,putanja):
        if(os.path.exists(putanja)):
            self.putanja = putanja
            self.extt = os.path.splitext(self.putanja)[1]
            print("putanja postoji.")
        else:
            print("putanja ne postoji.")

    def setPrvoPol(self,prvoPol):
        pretraga = self.sablon4.findall(prvoPol)
        print(pretraga)
        poluvreme = self.timeConverter.setVreme(pretraga)
        if (len(poluvreme.keys()) == 2):
            poluvreme = "00:{}:{},00".format(poluvreme["minut"],poluvreme["sekunda"])
            self.prvo_pol = int(self.timeConverter.konvert_u_sekunde(poluvreme))
            print(self.prvo_pol)
        else:
            print("greska3")
        
    def setDrugoPol(self,drugoPol):
        pretraga = self.sablon4.findall(drugoPol)
        poluvreme = self.timeConverter.setVreme(pretraga)
        if (len(poluvreme.keys()) == 2):
            poluvreme = "00:{}:{},00".format(poluvreme["minut"], poluvreme["sekunda"])
            self.drugo_pol = int(self.timeConverter.konvert_u_sekunde(poluvreme))
            print(self.drugo_pol)
        else:
            print("greska")
        
    def provera_fajla(self,fajl):
        video = self.checker.provera_fajla(fajl,self.sablon2,self.sablon3,
                                   self.prvo_pol,self.drugo_pol)
        if(str(type(video)) == "<class 'list'>"):
           for i in range(len(video)):
               pocetak = video[i][0]
               kraj = video[i][1]
               self.seckanje(i,pocetak,kraj)

        else:
            print("greska")
    def seckanje(self,br,pocetak,kraj):
        naziv = "video"+str(br)+self.extt
        ffmpeg_extract_subclip(self.putanja, pocetak, kraj, targetname=naziv)