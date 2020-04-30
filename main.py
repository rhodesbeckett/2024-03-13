from editor.FootballEditor import FootballEditor

fe = FootballEditor()
while(True):
    n = int(input(">>>"))
    if(n==1):
        fe.getPutanja("")
    elif(n==2):
        fe.provera_fajla("")
    elif(n==3):
        fe.setPrvoPol("05:09")
    elif(n==4):
        fe.setDrugoPol("59:40")
    elif(n==5):
        fe.seckanje()