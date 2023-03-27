
# — TRI SELECTION —
def tri_selection(list):
    n_comp = 0
    n_echange = 0
    n = len(list)
    if n > 1:
        for i in range(0, n-1):
            min = i
            for j in range(i+1, n):
                n_comp +=  1
                if list[j] < list[min]:
                    min = j
            list[i], list[min] = list[min], list[i]
            n_echange = n_echange + 1

    return {"list": list, "comp": n_comp, "echange": n_echange}

# — TRIE BULLES —
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

# – TRI PAR INSERTION —

# Fonctionne, par contre on crée une nouvelle liste sorted_lst, et on ajoute les elements par insertion
# La seule manière que j'ai trouvé de faire un tri par insertion avec les metodes inser() et remove().
def tri_insertion(lst):
    n_comp = 0
    n_echange = 0

    sorted_lst = [lst.pop(0)]
    for i in range(len(lst)):
        for j in range(len(sorted_lst)):
            n_comp += 1
            if lst[i] < sorted_lst[j]:
                n_echange += 1
                sorted_lst.insert(j, lst[i])
                break
        else:
            n_echange += 1
            sorted_lst.insert(len(sorted_lst), lst[i])
    return {"list": sorted_lst, "comp": n_comp, "echange": n_echange}

# Etat: Mauvais -> Fonctionne qu'avec des petites listes
def tri_insertion_2(lst):
    n_comp = 0
    n_echange = 0

    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            n_comp += 1
            lst.remove(key)
            lst.insert(j, key)
            n_echange += 1
            j -= 1
    return {"list": lst, "comp": n_comp, "echange": n_echange}

# Etat: Fonctionne 100%, par contre on n'utilise pas les métodes remove() et insert()
def tri_insertion_3(lst):
    n_comp_3 = 0
    n_echange_3 = 0

    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            n_comp_3 = n_comp_3 + 1
            lst[j+1] = lst[j]
            n_echange_3 = n_echange_3 + 1
            j -= 1
        lst[j+1] = key
        n_echange_3 = n_echange_3 + 1
    return {"list": lst, "comp": n_comp_3, "echange": n_echange_3}
    


