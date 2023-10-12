"""
Exercices: TP de NSI
"""

# 1)
def creer_file_vide():
    return []

def enfiler(l, x):
    l.append(x)

def defiler(l):
    return l.pop(0)

def lire_un_element():
    return l[0]

def file_est_vide(l):
    return len(l) == 0

# 2)
def affichage(l):
    liste_temp = list(l)
    while not file_est_vide(liste_temp):
        print(defiler(liste_temp))



# 3)
liste = []
enfiler(liste, 25)
enfiler(liste, 31)
enfiler(liste, 1)
enfiler(liste, 54)
enfiler(liste, 13)

enfiler(liste, 35)
defiler(liste)
defiler(liste)

print("Liste question 3:")
affichage(liste)

# 4)
def taille(file):
    f2 = creer_file_vide()

    count = 0
    while not file_est_vide(file):
        enfiler(f2, defiler(file))
        count = count + 1

    while not file_est_vide(f2):
        enfiler(file, defiler(f2))
    
    return count

# 5)
def dernier_element(liste):
    return liste[taille(liste) - 1]

# 7)

def enlever_dernier(liste):
    n = taille(liste)
    result = []
    f2 = []
    while not file_est_vide(liste):
        enfiler(f2, defiler(liste))
        if taille(result) == n - 1:
            result = 

    i = 0

    while i < taille(liste - 1):

