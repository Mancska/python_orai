#megoldas
def pontszamitas(lapok):
    ertek= 0
    for i in range(len(lapok)):
        ertek= +lapok[i]
    return ertek


def eredmeny(jatekos_laposzeg,gep_laposzeg):
    gepertek=pontszamitas(gep_laposzeg)
    jatekosertek=pontszamitas(jatekos_laposzeg)
    if jatekos_laposzeg>21:
        print("vesztet")
    if gep_laposzeg>21:
        print("vesztet")
#tesztesetek