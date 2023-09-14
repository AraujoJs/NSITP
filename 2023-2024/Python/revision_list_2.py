# TP NSI 1ère G. 2023-2024
# Tableaux et listes (Programmation Python)

import math, random

# c)
def moyenne(liste):
    somme = 0
    n = len(liste)
    for i in liste:
        somme = somme + i
    moy = somme / n
    return moy

# a)
mesures_y = [5.678, 7.765, 7.234, 6.567, 8.01, 4.902, 5.789]
# b)
somme_y = 0
for mesure in mesures_y:
    somme_y += mesure

moy_y = moyenne(mesures_y)
print("moy_y:", moy_y)


# d)
mesures_x = [3.475, 3.256, 3.621, 3.244, 3.132, 3.454, 3.585]
somme_x = 0
for mesure in mesures_x:
    somme_x += mesure

moy_x = moyenne(mesures_x)
print("moy_x:", moy_x)

# e)
ecarts = []
for mesure in mesures_x:
    ecarts.append(mesure - moy_x)
print("ecarts:", ecarts)

ecarts_au_carre = []
for mesure in mesures_x:
    ecarts_au_carre.append((mesure - moy_x)**2)

print("ecarts au carré:", ecarts_au_carre)

def sigma(first, last, x_moy):
    sum = 0
    for i in range(first,  last):
        sum += (mesures_x[i] - x_moy)**2
    return sum
        
n = len(mesures_x)
    
ecart_experimental = math.sqrt((sigma(0, n, moy_x) / (n - 1)))

print("Ecart principal:", ecart_experimental)

# 2)

valeurs = list()

for i in range(10):
    message = "Saisissez la valeur n°" + str(i+1) + ":"
    rep = int(input(message))
    valeurs.insert(0, rep)

print(valeurs)

# b)

random_list = []
plus_grand_count = 0
plus_petit = 0
for i in range(50):
    random_num = random.randint(0, 100)

    if i == 0:
        plus_petit = random_num
    
    if random_num < plus_petit:
        plus_petit = random_num

    random_list.append(random_num)
    if random_num > 50:
        plus_grand_count = plus_grand_count + 1

print("Random list:", random_list)
print("n de valeur > 50:", plus_grand_count)
print("plus petit:", plus_petit, " et sa position est:", random_list.index(plus_petit))
    



