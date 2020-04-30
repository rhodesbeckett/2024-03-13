from editor.FootballEditor import FootballEditor

fe = FootballEditor()
while(True):
    n = int(input(">>>"))
    if(n==1):
        fe.getPutanja("E:\\Projekat2\\projekat2-nrs\\Liverpool_-_Bournemouth.mkv")
    elif(n==2):
        fe.provera_fajla("")
    elif(n==3):
        fe.setPrvoPol("05:09")
    elif(n==4):
        fe.setDrugoPol("59:40")
    elif(n==5):
        fe.seckanje()