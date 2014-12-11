def islegit(x,y):
    return True

def Sammud(Potentsteelist):
    pikkus = len(Potentsteelist)
    zombitee = []
    i=1
    Suemanr1 = Potentsteelist[pikkus-i][1]
    zombitee.append(Potentsteelist[pikkus-1])
    while True:
        Suemanr2 = Potentsteelist[pikkus-i][0]
        if Suemanr2 == Suemanr1:
            zombitee.append(Potentsteelist[pikkus-i])
            i += 1
            Suemanr1 = Potentsteelist[pikkus-i][1]
        else:
            i += 1
        if Suemanr1 == 0:
            return zombitee[::-1]

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


def AI2(x,y,uusx,uusy,Ruudunr,Emanr,Potentsteelist,Proovilist,VähimF):
    if x == uusx and y == uusy:
        return Potentsteelist

    if islegit(uusx+1, uusy):
        G = Ge(Emanr,Potentsteelist)
        H = Ha(x,y,uusx+1,uusy)
        if [Ruudunr, Emanr, uusx+1,uusy,G,H] not in Potentsteelist and [Ruudunr, Emanr, uusx+1,uusy,G,H] not in Proovilist:
            Proovilist.append([Ruudunr,Emanr, uusx+1, uusy,G,H])
            Ruudunr += 1

    if islegit(uusx-1, uusy):
        G = Ge(Emanr,Potentsteelist)
        H = Ha(x,y,uusx-1,uusy)
        if [Ruudunr, Emanr, uusx-1,uusy,G,H] not in Potentsteelist and [Ruudunr, Emanr, uusx-1,uusy,G,H] not in Proovilist:
            Proovilist.append([Ruudunr,Emanr, uusx-1, uusy,G,H])
            Ruudunr += 1

    if islegit(uusx, uusy+1):
        G = Ge(Emanr,Potentsteelist)
        H = Ha(x,y,uusx,uusy+1)
        if [Ruudunr, Emanr, uusx,uusy+1,G,H] not in Potentsteelist and [Ruudunr, Emanr, uusx,uusy+1,G,H] not in Proovilist:
            Proovilist.append([Ruudunr,Emanr, uusx, uusy+1,G,H])
            Ruudunr += 1

    if islegit(uusx, uusy-1):
        G = Ge(Emanr,Potentsteelist)
        H = Ha(x,y,uusx,uusy-1)
        if [Ruudunr, Emanr, uusx,uusy-1,G,H] not in Potentsteelist and [Ruudunr, Emanr, uusx,uusy-1,G,H] not in Proovilist:
            Proovilist.append([Ruudunr,Emanr, uusx, uusy-1,G,H])
            Ruudunr += 1

 
    for F in Proovilist:
        if (F[4]+F[5])<= VähimF[1]:
            VähimF[1]=(F[4]+F[5])
            VähimF[0] = F[0]

        for neeger in Proovilist:
            if VähimF[0] == neeger[0]:
                pede = Proovilist.index(neeger)
                lits = Proovilist.pop(pede)
                Emanr = lits[0]
                uusx = lits[2]
                uusy = lits[3]
                Potentsteelist.append(lits)

    AI2(x,y,uusx,uusy,Ruudunr,Emanr,Potentsteelist,Proovilist,VähimF)
     
    
x = 7
y = 5
hordex = 12
hordey = 15

def AI(x,y,hordex,hordey):

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
    VähimF = [0,1000000]
    Emanr = Ruudunr
    Proovilist = []
    Potentsteelist = []
    
    
    Zombokordinaadid = [Ruudunr, Emanr-1, hordex, hordey,G,H]
    Potentsteelist.append(Zombokordinaadid)
    Ruudunr += 1
    
    AI2(x,y,uusx,uusy,Ruudunr,Emanr,Potentsteelist,Proovilist,VähimF)
    Path = []
    
    for samm in Sammud(Potentsteelist):
        Path.append([samm[2],samm[3]])
    
    return Path
    
print(AI(x,y,hordex,hordey))

