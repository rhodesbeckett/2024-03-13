import datetime
import time
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
import os.path
import re
# prvi str je source drugi je naziv iscek
class FootballEditor(object):
    putanja = ""
    prvo_pol = ""
    drugo_pol = ""
    sablonZaPoluvreme = re.compile("(\d{1,2}):(\d{1,2})(\S?|\s\d{1,2}?)")
    # sablonZaHighlights = re.compile("(\d{1,2}):(\d{1,2}) (\d{1,2}|\n")

    def getPutanja(self,putanja):
        if(os.path.exists(putanja)):
            self.putanja = putanja
            print("putanja postoji.")
        else:
            print("putanja ne postoji.")
    def setVreme(self, pretraga):
        info = {}
        if (len(pretraga) > 0):

            vreme = pretraga[0]
            for i in range(len(vreme)):
                # ako je samo jedna cifra tu dodati 0
                if (len(vreme[i]) < 2):
                    podatak = "0" + vreme[i]
                    if (i == 0):
                        info.setdefault("minut", podatak)
                    elif (i == 1):
                        info.setdefault("sekunda", podatak)
                    elif (i==2):
                        info.setdefault("do",vreme[i])
                # ako ima dva cifre onda ok
                elif(len(vreme[i]) == 2):
                    if (i == 0):
                        if(int(vreme[i])>99):

                            info = {}
                            break
                        else:
                            info.setdefault("minut", vreme[i])
                    elif (i == 1):
                        if (int(vreme[i]) >= 60):
                            print("greska2")
                            info = {}
                        else:
                            info.setdefault("sekunda", vreme[i])
                    elif (i==2):
                        info.setdefault("do",vreme[i])
            # vrati info ako postoje ovi parametri
            if ("minut" in info and "sekunda" in info):
                print(info)
                return info
        elif(len(pretraga)==0):
            return info
    def setPrvoPol(self,prvoPol):
        pretraga = self.sablonZaPoluvreme.findall(prvoPol)
        poluvreme = self.setVreme(pretraga)
        if (len(poluvreme.keys()) == 3):
            poluvreme = "00:{}:{},00".format(poluvreme["minut"],poluvreme["sekunda"])
            self.prvo_pol = self.konvert_u_sekunde(poluvreme)
            print(self.prvo_pol)
        else:
            print("greska3")
        
    def setDrugoPol(self,drugoPol):
        pretraga = self.sablonZaPoluvreme.findall(drugoPol)
        poluvreme = self.setVreme(pretraga)
        if (len(poluvreme.keys()) == 3):
            poluvreme = "00:{}:{},00".format(poluvreme["minut"], poluvreme["sekunda"])
            self.drugo_pol = int(self.konvert_u_sekunde(poluvreme))
            print(self.drugo_pol)
        else:
            print("greska")
        # self.drugo_pol = drugoPol
        
    def provera_fajla(self,fajl):
        print("ok")
    def konvert_u_sekunde(self,podatak):
        vreme = time.strptime(podatak.split(",")[0],"%H:%M:%S")
        sekunde1 = datetime.timedelta(hours=vreme.tm_hour,minutes=vreme.tm_min,seconds=vreme.tm_sec).total_seconds()
        return sekunde1
    def seckanje(self):
        # ffmpeg_extract_subclip(putanja, sekunde1, sekunde2, targetname="video1.mkv")
        print("okkk")
# class FootballEditor2(object):   
    # def __init__(self):
        # print("tu smo2!")