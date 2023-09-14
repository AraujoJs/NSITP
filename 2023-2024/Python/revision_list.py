print("Ex: 06")

semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

i = 0                   # Premier indice
j = len(semaine) - 1    # dernier indice

while i < j:
    semaine[i], semaine[j] = semaine[j], semaine[i]
    i += 1
    j -= 1


print("Liste enversée: ", semaine)
