"""
élève: ARAUJO José - 1G4
DS: Devoir programmation Tableau et algorithme glouton

"""

def rendu_monnaie_centimes(s_due, s_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre = s_versee - s_due
    i = len(pieces) - 1
    while a_rendre > 0:
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else :
            i = i - 1
    return rendu

def est_decroissant(tab):
    for i in range(len(tab)-1):
        if tab[i] < tab[i+1]:
            return False
    return True


"""
Exercice 1:
"""
print("-=-=-Exercice 1-=-=-:")
print(est_decroissant([9, 8, 5, 2, 0]))
print(est_decroissant([8, 12, 4]))
print(est_decroissant([4, -1]))
print(est_decroissant([5]))


print("\n-=-=-Exercice 2-=-=-:")

print(rendu_monnaie_centimes(700, 700))
print(rendu_monnaie_centimes(112,500))