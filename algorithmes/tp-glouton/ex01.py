"""
Exercice 1 : Problème du rendu de monnaie
Écrire et tester le programme Python permettant le rendu de monnaie proposé
dans le cours et le tester.
"""

print("*** Exercice 1:")

def get_pieces(m, p, n, i):
    while m > 0:
        if p[i] <= m:
            m -= p[i]
            n[i] += 1
        else:
            i += 1
    print(p)
    print(n)

p = [100, 50, 20, 10, 5, 2, 1]
n = [0, 0, 0, 0, 0, 0, 0]
i = 0

m = int(input("Valeur: "))

get_pieces(m, p, n, i)

"""
Notion de solution optimale
Avec les valeurs usuelles des pièces, la méthode donne un résultat juste et
généralement optimal. (un nombre de pièce minimum)
Cependant, étudions l’exemple (fictif) suivant :
o Pièces disponibles : 9 Euros, 8 Euros,1 Euro.
o Somme à rendre : 16 Euros
"""

def get_pieces_optimale(m, p, n, i):
    while m > 0:
        if p[i] <= m:
            m -= p[i]
            n[i] += 1
        else:
            i += 1
    print("\n -=-=- Notion de solution optimale -=-=- \n")
    print(f"montant: {m}€")
    print(p)
    print(n)

m = 16
p = [9, 8, 1]
n = [0, 0, 0]
i = 0

get_pieces_optimale(m, p, n, i)


"""
Exercice 2 : Problème du sac à dos
Un cambrioleur possède un sac à dos d'une contenance maximum de 40
Kg. Au cours d'un de ses cambriolages, il a la possibilité de dérober 4 objets
A, B, C , D, E, F. 
Voici un tableau qui résume les caractéristiques de ces objets: 

    objets :
        A B C D E F

    Valeurs en Euros: 
        30 12 12 12 12 4

    Poids en kg:
        39 10 10 10 10 1

a) Utiliser une méthode gloutonne pour déterminer « à la main » les objets
que le cambrioleur aura intérêt à dérober, afin d'optimiser son gain.

b) Refaire l'exercice en excluant la valeur A. Conclusion ?

c) Coder cet algorithme en python et tester le.

"""
print("\n*** Exercice 2: ")

def get_objets(items, data, sac, n):
    inside = []
    i = 0

    while sac > 0:
        item = items[i]

        if data[item]["poids"] <= sac:
            sac -= data[item]["poids"]
            inside.append(item)
        i += 1

    print(inside)

items = ["A", "B", "C", "D", "E", "F"]
data = {
    "A": {"valeur": 30, "poids": 39},
    "B": {"valeur": 12, "poids": 10},
    "C": {"valeur": 12, "poids": 10},
    "D": {"valeur": 12, "poids": 10},
    "E": {"valeur": 12, "poids": 10},
    "F": {"valeur": 4, "poids": 1}
    }

items2 = ["B", "C", "D", "E", "F"]
data2 = {
    "B": {"valeur": 12, "poids": 10},
    "C": {"valeur": 12, "poids": 10},
    "D": {"valeur": 12, "poids": 10},
    "E": {"valeur": 12, "poids": 10},
    "F": {"valeur": 4, "poids": 1}
    }

items3 = ["A","B","C","D","E","F","G","H","I","J", "K", "L","M","N" ]

data3 = {
    "A": {"valeur": 4, "poids": 2},
    "B": {"valeur": 3, "poids": 2},
    "C": {"valeur": 8, "poids": 5},
    "D": {"valeur": 5, "poids": 2},
    "E": {"valeur": 10, "poids": 7},
    "F": {"valeur": 7, "poids": 4},
    "G": {"valeur": 1, "poids": 1},
    "H": {"valeur": 6, "poids": 4},
    "I": {"valeur": 3, "poids": 2},
    "J": {"valeur": 3, "poids": 1},
    "K": {"valeur": 6, "poids": 4},
    "L": {"valeur": 12, "poids": 20},
    "M": {"valeur": 2, "poids": 2},
    "N": {"valeur": 4, "poids": 1}

}


sac = 40
sac3 = 26

n = 4

print("\nA) Les objets:")
get_objets(items, data, sac, n)
print("\nB) Les objets:")
get_objets(items2, data2, sac, n)

print("\nC) Les objets:")
get_objets(items3, data3, sac3, n)
