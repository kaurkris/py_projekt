##    for i in range(len(hordex)):
##        zx=randint(-1,1)
##        zy=randint(-1,1)
##        if isfree(hordex[i],hordey[i],zx,0):
##            hordex[i]+=zx
##        if isfree(hordex[i],hordey[i],0,zy):
##            hordey[i]+=zy

#hordex = zombide x kordinaadid
#hordey = zombide y kordinaadid
#x = kuti x kordinaat
#y = kuti y kordinaat
def islegit(x,y):
    return True

def Ge(Emanr,Potentsteelist):
    G = 10
    for i in Potentsteelist:
        if i[0] == Emanr:
            G += i[4]
    return G
def Ha(x,y,ux,uy):
    lolx = abs(x-ux)
    loly = abs(y-uy)
    return ((loly+lolx)*10)
##Potentsteelist=[[0,-1,1,1,0],[1,0,1,1,10],[2,1,1,1,20]]
##print(G(1,Potentsteelist))

def AI2(x,y,uusx,uusy,Ruudunr,Emanr,Potentsteelist,Proovilist,VähimF):

    if x == uusx and y == uusy:
        return Potentsteelist
    if islegit(uusx-1, uusy):
        G = Ge(Emanr,Potentsteelist)
        H = Ha(x,y,uusx+1,uusy)
        Proovilist.append([Ruudunr,Emanr, uusx+1, uusy,G,H])
        Ruudunr += 1
    if islegit(uusx-1, uusy):
        G = Ge(Emanr,Potentsteelist)
        H = Ha(x,y,uusx-1,uusy)
        Proovilist.append([Ruudunr,Emanr, uusx-1, uusy,G,H])
        Ruudunr += 1
    if islegit(uusx, uusy+1):
        G = Ge(Emanr,Potentsteelist)
        H = Ha(x,y,uusx,uusy+1)
        Proovilist.append([Ruudunr,Emanr, uusx, uusy+1,G,H])
        Ruudunr += 1
    if islegit(uusx, uusy-1):
        G = Ge(Emanr,Potentsteelist)
        H = Ha(x,y,uusx,uusy-1)
        Proovilist.append([Ruudunr,Emanr, uusx, uusy-1,G,H])
        Ruudunr += 1
        
    for F in Proovilist:
        if (F[4]+F[5])<=VähimF[1]:
            VähimF[1]=(F[4]+F[5])
            VähimF[0] = F[0]
            print(VähimF)

    for neeger in Proovilist:
        if VähimF[0] == neeger[0]:
            lits = Proovilist.pop()
            Ruudunr = lits[0]
            Emanr = lits[1]
            uusx = lits[2]
            uusy = lits[3]
            Potentsteelist.append(lits)

    AI2(x,y,uusx,uusy,Ruudunr,Emanr,Potentsteelist,Proovilist,VähimF)
     
    
x = 7
y = 5
def AI(x,y):
    hordex = 1
    hordey = 1 #hiljem global ette
    uusx = hordex
    uusy = hordey
    
    #zombo kordinaadid(A) kohaleidmislisti
    #zombo ümber olevad kordinaadid kohaleidmislisti + märkida ära, et nad olid A ümber(vanemad)
    #A listist välja ja 2.listi
    #Kõigile ümberolevatele ruutudele G ja H väärtused
    #G on kõigi otse minemiseks 10 ja diagonaalis 14 + vanema G
    #H on linnulennult kõik ruudud mis vaja on, et kohale jõuda sealt ruudult x10
    #F on G+H mille järgi otsustame kuhu me läheme
    #Siis valmine ruudu, kus on kõige väiksem F, litime selle 2. listi
    #vaatame kõigi ümberringi olevate ruutude Fi ja märgime ära kes nende 'vanem' on
    #(ruut ei tohi olla 1. ega 2. listis)
    
    Ruudunr = 0
    G = 0
    H = 0
    VähimF = [0,1000000]#kole aga töötab seega#yolo
    Emanr = Ruudunr
    Proovilist = []
    Potentsteelist = []
    
    
    Zombokordinaadid = [Ruudunr, Emanr-1, hordex, hordey,G,H]
    #Proovilist.append(Zombokordinaadid)
    Potentsteelist.append(Zombokordinaadid)
    Ruudunr += 1
    z = AI2(x,y,uusx,uusy,Ruudunr,Emanr,Potentsteelist,Proovilist,VähimF)
##    if islegit(uusx-1, uusy):
##        G = Ge(Emanr,Potentsteelist)
##        H = Ha(x,y,uusx+1,uusy)
##        Proovilist.append([Ruudunr,Emanr, uusx+1, uusy,G,H])
##        Ruudunr += 1
##    if islegit(uusx-1, uusy):
##        G = Ge(Emanr,Potentsteelist)
##        H = Ha(x,y,uusx-1,uusy)
##        Proovilist.append([Ruudunr,Emanr, uusx-1, uusy,G,H])
##        Ruudunr += 1
##    if islegit(uusx, uusy+1):
##        G = Ge(Emanr,Potentsteelist)
##        H = Ha(x,y,uusx,uusy+1)
##        Proovilist.append([Ruudunr,Emanr, uusx, uusy+1,G,H])
##        Ruudunr += 1
##    if islegit(uusx, uusy-1):
##        G = Ge(Emanr,Potentsteelist)
##        H = Ha(x,y,uusx,uusy-1)
##        Proovilist.append([Ruudunr,Emanr, uusx, uusy-1,G,H])
##        Ruudunr += 1
##        
##    for F in Proovilist:
##        if (F[4]+F[5])<=VähimF[1]:
##            VähimF[1]=(F[4]+F[5])
##            VähimF[0]=F[0]
##            print(VähimF)
##
##    for neeger in Proovilist:
##        if VähimF[0] == neeger[0]:
##            Potentsteelist.append(Proovilist.pop())

    

    #Litib kõik liigutavad suunad listi
        
##    for jobu in Proovilist:
##        print(jobu)
    print(z)
AI(7,5)

