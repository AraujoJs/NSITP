# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 14:06:55 2023

@author: j.dearaujofirmino
"""

fournitures = {"Cahier 100 pages": 2.25,
               "100 coipes A4": 3.75,
               "Lot 4 stylos bille": 3.5,
               "Papier imprimante 500 feuilles": 4.5
               }
print(fournitures.keys())

print(fournitures.values())


itens = fournitures.items()

le_plus_cher = ()

count = 0.0
for cle, value in itens:
    if value > count:
        le_plus_cher = (cle, value)

print(f"Produit: {le_plus_cher[0]} \nprix: {le_plus_cher[1]} €")


# Exercice 2:

nombres = {"0":"zero","1":"un", "2":"deux", "3":"trois", "4":"quatre",
           "5":"cinq", "6":"six", "7":"sept", "8":"huit", "9":"neuf"}

string = "j'ai 3 pommes et 2 bananes et 5 poires"

for lettre in string:
    if lettre in nombres:
        string = string.replace(lettre, nombres[lettre])

print(string)

# Exercice 3:

adresses = {"Paul Dupont": "3, Boulevard de la Convention", 
            "Aline Dubois": "10, Avenue de la Gare",
            "Linda Marchand": "36, rue de la Chimie",
            "Salvatore Rizzi": "14, rue de la Romanche"}

nom = str(input("saisissez votre nom: "))
if(nom in adresses):
    print(f"Votre adresse est {adresses[nom]}")
else:
    print("Non référencé")

# Exercice 4:

def freqChaine(string):
    dictionnaire = {}
    for lettre in string:
        if (lettre not in dictionnaire):
            dictionnaire[lettre] = string.count(lettre)
    return dictionnaire

phrase = str(input())
dic = freqChaine(phrase.strip())
print(dic)

