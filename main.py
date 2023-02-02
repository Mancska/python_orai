# megoldas
def pontokosszege2(lapok: [int]):
    pontok: int = 0
    for i in range(len(lapok)):
        pontok += lapok[i]

    return pontok


def eredmeny(gLapok: [int], jLapok: [int]):
    jPontok: int = pontokosszege2(jLapok)
    gPontok: int = pontokosszege2(gLapok)
    vegeredmeny = ""
    if jPontok and gPontok > 21:
        vegeredmeny = "mindenki vesztett"
    elif gPontok > 21:
        vegeredmeny = "gép vesztett"
    elif jPontok > 21:
        vegeredmeny = "játékos vesztett"

    return vegeredmeny

# teszt esetek
def tesztesetek():
    if jatekos_vesztett_teszt():
        print("jatékosvesztet")
    else:
        print("jatékos nyert")

def nagyobb_mint_21(Jpontokosszege2,Gpontokosszege2):
    if Jpontokosszege2>21:
        print("jatékos vesztet")
    if Gpontokosszege2>21:
        print("gép vesztet")
def ki_van_közelebb(Jpontokosszege2,Gpontokosszege2):
    if Jpontokosszege2>Gpontokosszege2:
        print("jatékos van közelebb")
    if Gpontokosszege2>Jpontokosszege2:
        print("gép van közelebb")

def jatekos_vesztett_teszt():
    jatekos = [10, 9, 3]
    gep = [10, 6]
    vart_eredmeny = "játékos vesztett"
    kapott_eredmeny = eredmeny(gep,jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("a teszt sikeres")
        return True
    else:
        print("a teszt megbukott")
        return False
def gep_vesztett_teszt():
    jatekos = [10, 9, 3]
    gep = [10, 6]
    vart_eredmeny = "gép vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("a teszt sikeres")
        return True
    else:
        print("a teszt megbukott")
        return False
tesztesetek()