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
    nrn = file.readline().rstrip("\n")
    for i in range(int(nrn)):
        leg = []
        lit = []
        # stare =  ("Stare nod i")
        stare = file.readline().rstrip("\n")
        # nrm =  ("Nr. de legaturi ale nodului i"
        nrm = file.readline().rstrip("\n")
        for j in range(int(nrm)):
            # leg.append = "ID nod cu care se leaga nodul i"
            leg.append(file.readline().rstrip("\n"))
            # lit.append="Litera acceptata pe legatura [i, leg[j]]"
            lit.append(file.readline().rstrip("\n"))
        M = Muchie(leg, lit)
        N = Nod(stare, nrm, M)
        automat.append(N)


def verifica_cv(automat, cuvant):
    ok = 1
    nod = 0
    numar_legaturi_verificate = 0
    indexMuchie = None
    indexAlegerePrecedenta = None
    while int(automat[nod].nrm) > numar_legaturi_verificate:
        numar_legaturi_verificate = 0
        for c in cuvant:
            lista_ponderi = automat[nod].Muchie.litera
            lista_legaturi = automat[nod].Muchie.leg
            result = None
            result = [litere_multiple for litere_multiple in lista_ponderi if c in litere_multiple]
            if c in lista_ponderi:
                if indexMuchie is not None:
                    indexAlegerePrecedenta = indexMuchie
               # indexMuchie = [index for index, litera in enumerate(lista_ponderi) if litera is c and index is not indexAlegerePrecedenta]
                indexMuchie = lista_ponderi.index(c)
                nodVechi = nod

                nod = int(lista_legaturi[indexMuchie])
            elif result is not None:
                result = ", ".join(result)
                print(result)
                if indexMuchie is not None:
                    indexAlegerePrecedenta = indexMuchie
                indexMuchie = lista_ponderi.index(result)
                nodVechi = nod
                nod = int(lista_legaturi[indexMuchie])
            else:
                ok = 0
                break
    if ok == 1 and automat[nod].stare is 'finala':
        print ("Cuvant acceptat")
    elif ok == 0 and automat[nod].stare is 'finala' and cuvant is '':
        print ("Cuvant acceptat")
    else:
        print ("Cuvant respins")


'''
# Functia main
# 1) Deschid fisierul afn.in
# 2) Apelez functia de citire automat
# 3) Stochez cuvantul de verificat
# 4) Apelez functia de verificare cuvant
'''


if __name__ == "__main__":
    file = open("afn.in", "r")
    automat = []
    citire_automat(automat)
    cuvant = "abbbac"
    verifica_cv(automat, cuvant)
