"""
Exercice 2 : Problème du sac à dos
1) Présentation du problème
Un cambrioleur possède un sac à dos d'une contenance maximum de 40
Kg. Au cours d'un de ses cambriolages, il a la possibilité de dérober 4 objets
A, B, C , D, E, F. Voici un tableau qui résume les caractéristiques de ces objets :

                Objets: A B C D E F

Valeurs en
Euros 30 12 12 12 12 4
Poids en kg 39 10 10 10 10 1
a) Utiliser une méthode gloutonne pour déterminer « à la main » les objets
que le cambrioleur aura intérêt à dérober, afin d’optimiser son gain.
b) Refaire l’exercice en excluant la valeur A. Conclusion ?
c) Coder cet algorithme en python et tester le.
"""

from random import randint


def essence(liste, dmax):
    n=len(liste)
    d=dmax
    stations=[]
    i=0
    while i != n:
        while i<n and liste[i]<=d:
            d = d - liste[i]
            i = i + 1
            stations.append(i - 1)
            d = dmax
        
        return stations

def somme(liste):
    somme = 0
    for i in liste:
        somme += i

trajet = int(input("Trajet:"))
reservoir = int(input("Reservoir: "))


tab = randint(25, 50)

while 

print(tab)