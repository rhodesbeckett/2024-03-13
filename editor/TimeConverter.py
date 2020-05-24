import datetime
import time
class TimeConverter(object):
    def setVreme(self, pretraga):
        print(pretraga)
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
                        if(int(vreme[i])>59 and int(vreme[i])<100):
                            minut = int(vreme[i])-60
                            info.setdefault("sat","01")
                            if(minut<10):
                                minut = "0"+str(minut)
                            info.setdefault("minut",str(minut))
                            # info = {}
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
                if("sat" not in info):
                    info.setdefault("sat","00")
                return info
        elif(len(pretraga)==0):
            return info
    def konvert_u_sekunde(self,podatak):
        vreme = time.strptime(podatak.split(",")[0],"%H:%M:%S")
        sekunde1 = datetime.timedelta(hours=vreme.tm_hour,minutes=vreme.tm_min,seconds=vreme.tm_sec).total_seconds()
        return sekunde1