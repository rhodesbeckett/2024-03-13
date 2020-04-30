from editor.TimeConverter import *
class Checker(object):
    sablon = ""
    tc = TimeConverter()
    def provera_fajla(self, fajl, sablon2, sablon3,prvoPol,drugoPol):

        # E:\Projekat2\projekat2-nrs\highlights.txt
        fajl = open(fajl)
        linija = fajl.readline()
        vremena_u_sekundama = []
        poluvreme = 0
        while(linija!=""):
            if(linija == "11\n"):
                poluvreme = 1
            elif(linija == "22\n"):
                poluvreme = 2
            pretraga = sablon2.findall(linija)
            if(len(pretraga)>0):
                if(len(pretraga[0]) == 4):
                    # print(pretraga[0][0:2])
                    pocetak = self.tc.setVreme((pretraga[0][0:2],))
                    kraj = self.tc.setVreme((pretraga[0][2:4],))
                    if(poluvreme == 1):
                        pocetak = prvoPol+self.getSekunde(pocetak)
                        kraj = prvoPol+self.getSekunde(kraj)
                    elif (poluvreme == 2):
                        pocetak = drugoPol + self.getSekunde(pocetak)
                        kraj = drugoPol + self.getSekunde(kraj)
                    vremena_u_sekundama.append((pocetak,kraj))

            elif(len(pretraga) == 0):
                if (linija != "11\n" or linija != "22\n"):
                    pretraga3 = sablon3.findall(linija)
                    pocetak = self.tc.setVreme(pretraga3)


            linija = fajl.readline()
        fajl.close()
        return vremena_u_sekundama
    def provera_putanje(self):
        print("ok")
    def provera_prvog_pol(self,fajl):
       print("ok")

    def provera_drugog_pol(self):
        print("ok")
    def getSekunde(self,podatak):
        if (len(podatak.keys()) == 2):
            podatak = "00:{}:{},00".format(podatak["minut"], podatak["sekunda"])
            podatak = int(self.tc.konvert_u_sekunde(podatak))
            return podatak
