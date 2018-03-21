class Muchie:
    def __init__(self, leg, litera):
        self.leg = leg
        self.litera = litera

class Nod:
    def __init__(self, stare, nrm, Muchie):
        self.stare = stare
        self.nrm = nrm
        self.Muchie = Muchie

def citire_automat(automat):
    for i in range(int(nrn)):
        leg = []
        lit = []
        stare = file.readline().rstrip("\n")#stare = input ("Stare nod " + str(i) + ":")
        nrm = file.readline().rstrip("\n")#nrm = input ("Nr. de legaturi ale nodului " + str(i) + ":")
        for j in range(int(nrm)):
            leg.append(file.readline().rstrip("\n"))#leg.append( input ("ID nod cu care se leaga nodul " + str(i) + ":") )
            lit.append(file.readline().rstrip("\n"))#lit.append( input ("Litera acceptata pe legatura [" + str(i) + "," + str(leg[j]) + "] : ")  )
        M = Muchie(leg, lit)
        N = Nod(stare, nrm, M)
        automat.append(N)

def verifica_cv(automat, cuvant):
    ok = 1
    nod = 0
    for c in cuvant:
        lista_ponderi = automat[nod].Muchie.litera
        lista_legaturi = automat[nod].Muchie.leg
        if c in lista_ponderi:
            indexMuchie = lista_ponderi.index(c)
            nod = int(lista_legaturi[indexMuchie])
        else:
            ok = 0
            break
    if ok==1 and automat[nod].stare is 'f':
        print ("Cuvant acceptat")
    elif ok==0 and automat[nod].stare is 'f' and cuvant is '':
        print ("Cuvant acceptat")
    else:
        print ("Cuvant respins")
'''
# Functia main
# 1) Deschid fisierul automat.in
# 2) Citesc din fisier numarul de noduri
# 3) Apelez functia de citire automat
# 4) Stochez cuvantul de verificat
# 5) Apelez functia de verificare cuvant
'''
if __name__ == "__main__":
    file = open("automat.in", "r")
    nrn = file.readline().rstrip("\n")
    automat = []
    citire_automat(automat)
    cuvant = "bbbabb"
    verifica_cv(automat, cuvant)

