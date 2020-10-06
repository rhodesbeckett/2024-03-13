class Seconds(object):


	def convertToSeconds(self,entry,tip):
		entry = str(entry)
		zero = False
		sekunde = 0
		while True:
			if len(entry)>0 and len(entry)<4:
				if entry.isdigit():
					if entry.startswith("0") and len(entry)>2:
						# npr 023
						print("greska")
						break
					if entry.startswith("0") and len(entry) <= 2:
						# 01
						zero = True
					if tip == "minut":
						if zero == True:
							if len(entry)==1:
								sekunde = int(entry[0])
							elif len(entry)==2:
								sekunde = int(entry[1])*60
						else:
							sekunde = int(entry)*60
						return sekunde
					elif tip == "sekunda":
						if len(entry)==3:
							print("greska")
							break
						if zero == True:
							if len(entry)==2:
								sekunde = int(entry[1])
							else:
								sekunde =  int(entry[0])
						else:
							if int(entry)>60:
								print("greska")
								print("evo")
								break
							sekunde = int(entry)
						return sekunde
				break
			break

	def convertBoth(self,poluvreme):
		minut = self.convertToSeconds(poluvreme["minut"], "minut")
		sekunda = self.convertToSeconds(poluvreme["sekunda"],"sekunda")
		return minut,sekunda
