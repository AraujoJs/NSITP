"""
Rappels sur les dictionnaires
ARAUJO José - TG4 (NSI)
Exercices:
"""
# 1)

fournitures = {
    "Cahier 100 pages": 2.25, 
    "100 copies A4": 3.75, 
    "Lot 4 stylos bille": 3.5, 
    "Papier imprimante 500 feuilles": 4.5
    }
print("Les clés:")
for prod in fournitures.keys():
    print(prod)

print("\nLes prix:")
for prix in fournitures.values():
    print(prix)

plus_cher = ("", 0)
for (item, prix) in fournitures.items():
    if prix > plus_cher[1]:
        plus_cher = (item, prix)

print("\nLe plus cher:")
print(plus_cher)

# 2)
nombres = {
    0: "zero", 
    1: "un", 
    2: "deux", 
    3: "trois", 
    4: "quatre", 
    5: "cinq", 
    6: "six", 
    7: "septe", 
    8: "huit", 
    9: "neuf"
    }
phrase = "J'ai 3 pommes et 2 bananes"

def num_en_mot(phrase, num):
    new_phrase = ""
    for mot in phrase.split(" "):
        if mot in [str(cle) for cle in num]:
            new_phrase += num[int(mot)] + " "
        else:
            new_phrase += mot + " "
    return new_phrase.strip()

print("\nPhrase:\n" + phrase)
print(num_en_mot(phrase, nombres))

# 3)

adresses = {
    "Paul Dupont": (3, "Boulevard de la Convention"),
    "Aline Dubois": (10, "Avenue de la Gare"),
    "Linda Marchand": (36, "rue de la Chimie"),
    "Salvatore Rizzi": (14, "rue de la Romanche")
}

def chercher_adress(nom: str, adresses: dict):
    if nom in adresses:
        adresse = adresses[nom]
        print(f"L'adresse de {nom}:\nN°{adresse[0]}, rue {adresse[1]}")
    else:
        print("Non référencé")

chercher_adress(input("\nNom que vous souhaitez chercher: ").strip(), adresses)

