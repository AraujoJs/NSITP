"""
- Controle sur les tris -

ARAUJO José
1G4 - NSI

"""

def tri_ameliore(ta):
    n_comp = 0
    n_echange = 0

    n = len(ta)
    intervale = n - 1
    echange_valeur = True
    print(ta)
    while echange_valeur or intervale > 1:

        if intervale > 1:
            intervale = int(intervale / 1.3)
        echange_valeur = False
        for i in range(0, n-intervale):
            n_comp += 1
            if ta[i] > ta[i + intervale]:
                ta[i], ta[i+intervale] = ta[i+intervale], ta[i]
                print(ta)
                echange_valeur = True
    return ta

list = [5, 4, 7, 9, 1, 3, 2]
print(tri_ameliore(list))