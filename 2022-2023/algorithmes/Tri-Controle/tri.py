"""
- Controle sur les tris -

ARAUJO José
1G4 - NSI

"""

def tri_bulles(list):
    n = len(list)
    n_comp = 0
    n_echange = 0
    if n > 1:
        for j in range(0, n):
            for i in range(0, n-1-j):
                n_comp += 1
                if list[i] > list[i+1]:
                    list[i], list[i+1] = list[i+1], list[i]
                    n_echange += 1

    return {"list": list, "comp": n_comp, "echange": n_echange}

def tri_ameliore(ta):
    n_comp = 0
    n_echange = 0

    n = len(ta)
    intervale = n - 1
    echange_valeur = True
    while echange_valeur or intervale > 1:
        if intervale > 1:
            intervale = int(intervale / 1.3)
        echange_valeur = False
        for i in range(0, n-intervale):
            n_comp += 1
            if ta[i] > ta[i + intervale]:
                n_echange += 1
                ta[i], ta[i+intervale] = ta[i+intervale], ta[i]
                echange_valeur = True
    return {"list": ta, "comp": n_comp, "echange": n_echange}

def comparer_tri(ameliore, bulles, lst):
    dic_ameliorer = ameliore(list(lst))
    dic_bulles = bulles(list(lst))

    if (dic_ameliorer['echange'] < dic_bulles['echange']) or (dic_ameliorer['echange'] == dic_bulles['echange'] and dic_ameliorer['comp'] < dic_bulles['comp']):
        dic_ameliorer['name'] = 'Tri amelioré'
        format_result(dic_ameliorer, dic_bulles)
        
    else:
        dic_bulles['name'] = 'Tri à bulle'

        format_result(dic_bulles, dic_bulles)

def format_result(dic, m_dic):
    print('\n -=- LE PLUS EFFICIENT -=-\n')
    print(f"Tri: {dic['name']}")
    print(f"Numero d'echanges: {dic['echange']} (l'autre tri: {m_dic['echange']})")
    print(f"Numero de comparaison: {dic['comp']} (l'autre tri: {m_dic['comp']})")


lst = [5, 4, 7, 9, 1, 3, 2]

gts = [251, 967, 862, 548, 204, 678, 750, 998, 568, 416, 630, 270, 40, 653, 360, 721, 178, 158, 300, 914, 34, 
       439, 24, 51, 815, 690, 345, 222, 398, 58]
print(tri_bulles(list(lst)))
print(tri_ameliore(list(lst)))
result = comparer_tri(tri_ameliore, tri_bulles, gts)