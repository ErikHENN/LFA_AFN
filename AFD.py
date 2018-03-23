class Muchie:
    def __init__(self, legatura, litera):
        self.legatura = legatura
        self.litera = litera


class Nod:
    def __init__(self, stare, nrm, Muchie):
        self.stare = stare
        self.nrm = nrm
        self.Muchie = Muchie


'''
clasa Nod reprezinta caracteristicile unui nod al automatului, stare, numarul de legaturi (nrm) si Muchia de legatura 
cu ale sale caracteristici definite in clasa Muchie (id-ul nodului cu care se leaga muchia si
 litera transmisa prin intermediul ei). 
Deci pentru fiecare nod din automat voi citi NRM legaturi, ale caror caracteristici sunt stocate in listele
 de adiacenta (leg, lit) 
ale clasei Muchie pe pozitii similare. Dupa citirea datelor fiecarui nod, 
retin obiectul de tip nod in lista de obiecte automat,
unde voi avea practic graful cu toate caracteristicile necesare.
'''


def citire_automat(automat):
    nrn = file.readline().rstrip("\n")
    for i in range(int(nrn)):
        legatura = []
        litera = []
        # stare =  ("Stare nod i")
        stare = file.readline().rstrip("\n")
        # nrm =  ("Nr. de legaturi ale nodului i"
        nrm = file.readline().rstrip("\n")
        for j in range(int(nrm)):
            # leg.append = "ID nod cu care se leaga nodul i"
            legatura.append(file.readline().rstrip("\n"))
            # lit.append="Litera acceptata pe legatura [i, leg[j]]"
            litera.append(file.readline().rstrip("\n"))
        M = Muchie(legatura, litera)
        N = Nod(stare, nrm, M)
        automat.append(N)


'''
Aici initializez variabila ok cu 1 (presupun ca va accepta cuvantul) si plec de la nodul 0 (starea initiala). 
Pentru fiecare litera din cuvant verific daca se afla in lista de ponderi ai nodului 
(daca nodul are vreo legatura care accepta litera din cuvant), prin linia indexMuchie = lista_ponderi.index(c), 
unde functia index(c) returneaza pozitia (indexul) caracterului c in lista de ponderi, care reprezinta a N-a muchie 
(unde N este variabila indexMuchie) ce se identifica cu nodul de legatura. In caz contrar, 
daca caracterul c nu se afla in lista de ponderi variabila ok va deveni 0 si cuvantul va fi respins.

In final avem 3 verificari: if ok==1 and automat[nod].stare is 'f': - Daca au fost acceptate toate literele din cuvant 
si s-a ajuns in stare finala elif ok==0 and automat[nod].stare is 'f' and cuvant is '': 
- Daca nu au fost acceptate toate literele cuvantului dar s-a ajuns in stare finala, 
adica automatul va accepta cuvantul vid. Altfel cuvantul va fi respins
'''


def verifica_cv(automat, cuvant):
    ok = 1
    nod = 0
    for c in cuvant:
        lista_ponderi = automat[nod].Muchie.litera
        lista_legaturi = automat[nod].Muchie.legatura
        if c in lista_ponderi:
            indexMuchie = lista_ponderi.index(c)
            nod = int(lista_legaturi[indexMuchie])
        else:
            ok = 0
            break
    if ok == 1 and automat[nod].stare is 'f':
        print ("Cuvant acceptat")
    elif ok == 0 and automat[nod].stare is 'f' and cuvant is '':
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
    file = open("afd.in", "r")
    automat = []
    citire_automat(automat)
    cuvant = "bbabaaa"
    verifica_cv(automat, cuvant)