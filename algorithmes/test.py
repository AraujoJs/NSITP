import random
from tri import tri_selection, tri_bulles, tri_insertion, tri_insertion_2, tri_insertion_3
from colorama import init, Fore, Back, Style



def get_most_efficient(list):
    most_efficient = {}

    print("-=-"*5 + "MOST EFFICENT" + "-=-" *5)

    print("tri selection:")
    dic = test(tri_selection, list)
    comp_selection = dic["comp"]
    echange_selection = dic["echange"]
    print(dic["list"])
    print(f"N° comparaison: {comp_selection} \nN° d'echange: {echange_selection}\n")
    most_efficient['most_comp'] = comp_selection
    most_efficient['most_echange'] = echange_selection
    most_efficient['most_name'] = "tri par selection"
    most_efficient['most_desc'] = """
    Le tri par sélection est considéré comme inefficace pour les grandes listes, 
    car sa complexité temporelle est de l'ordre de O(n^2), mais il peut être utile 
    pour les petites listes ou pour trier des fichiers en mémoire externe.
    """


    print("tri bubble:")
    dic = test(tri_bulles, list)
    comp_bubble = dic["comp"]
    echange_bubble = dic["echange"]
    print(dic["list"])
    print(f"N° comparaison: {comp_bubble} \nN° d'echange: {echange_bubble}\n")
    if echange_bubble < most_efficient['most_echange'] or (echange_bubble == most_efficient['most_echange'] and comp_bubble < most_efficient['most_comp']):
        most_efficient['most_comp'] = comp_bubble
        most_efficient['most_echange'] = echange_bubble
        most_efficient['most_name'] = "tri à Bulle"
        most_efficient['most_desc'] = """
        Le tri à bulle, à chaque itération, le plus grand élément de la liste se déplace progressivement 
        vers sa position finale, en remontant "à la surface" comme une bulle, d'où le nom 
        "tri à bulle". Le tri à bulle est un algorithme de tri simple mais inefficace pour 
        les listes de grande taille, car il peut prendre beaucoup de temps pour trier une 
        liste si celle-ci est longue.
"""

    print("tri insertion[case 1]:")
    dic = test(tri_insertion, list)
    comp_insert = dic["comp"]
    echange_insert = dic["echange"]
    print(dic["list"])
    print(f"N° comparaison: {comp_insert} \nN° d'echange: {echange_insert}\n")
    if echange_insert < most_efficient['most_echange'] or (echange_insert == most_efficient['most_echange'] and comp_insert < most_efficient['most_comp']):
        most_efficient['most_comp'] = comp_insert
        most_efficient['most_echange'] = echange_insert
        most_efficient['most_name'] = "tri par insertion [cas n° 1]"
        most_efficient['most_desc'] = """
        Le tri par insertion est un algorithme de tri simple qui fonctionne en parcourant 
        une liste d'éléments à trier, en insérant chaque élément à sa place appropriée dans 
        une liste triée en construction. Lorsque le processus est terminé, la liste triée est 
        renvoyée.
        """

    print("tri insertion[case 2]:")
    dic = test(tri_insertion_2, list)
    comp_insert_2 = dic['comp']
    echange_insert_2 = dic['echange']
    print(dic["list"])
    print(f"N° comparaison: {comp_insert_2} \nN° d'echange: {echange_insert_2}\n")
    if echange_insert_2 < most_efficient['most_echange'] or (echange_insert_2 == most_efficient['most_echange'] and comp_insert_2 < most_efficient['most_comp']):
        most_efficient['most_comp'] = comp_insert_2
        most_efficient['most_echange'] = echange_insert_2
        most_efficient['most_name'] = "tri par insertion [cas n° 2]"
        most_efficient['most_desc'] = """Le tri par insertion est un algorithme de tri simple 
        qui fonctionne en parcourant une liste d'éléments à trier, en insérant chaque élément 
        à sa place appropriée dans une liste triée en construction. Lorsque le processus est 
        terminé, la liste triée est renvoyée.
        """

    print("tri insertion[case 3]:")
    dic = test(tri_insertion_3, list)
    comp_insert_3 = dic['comp']
    echange_insert_3 = dic["echange"]
    print(dic['list'])
    print(f"N° comparaison: {comp_insert_3} \nN° d'echange: {echange_insert_3}\n")
    if echange_insert_3 < most_efficient['most_echange'] or (echange_insert_3 == most_efficient['most_echange'] and comp_insert_3 < most_efficient['most_comp']):
        most_efficient['most_comp'] = comp_insert_3
        most_efficient['most_echange'] = echange_insert_3
        most_efficient['most_name'] = "tri par insertion [cas n° 3]"
        most_efficient['most_desc'] = """Le tri par insertion est un algorithme de tri simple 
        qui fonctionne en parcourant une liste d'éléments à trier, en insérant chaque élément 
        à sa place appropriée dans une liste triée en construction. Lorsque le processus est 
        terminé, la liste triée est renvoyée.
        """

    print(Fore.YELLOW + "—=- MOST EFICIENT:" + Fore.RESET)
    print(f"""

    {Fore.GREEN + "Le plus efficace tri:" + Fore.RESET} 
    {Fore.BLUE + Style.BRIGHT + most_efficient['most_name'] + Fore.RESET + Style.RESET_ALL}
    {Fore.GREEN + "n° de comparaisons:" + Fore.RESET} {Fore.RED + str(most_efficient['most_comp']) }
    {Fore.GREEN + "n° d'echanges:" + Fore.RESET} {Fore.RED + str(most_efficient['most_echange']) + Fore.RESET}
    {Fore.GREEN + most_efficient['most_desc'] + Fore.GREEN}
    """
          )
    
    print(Fore.YELLOW + "-=- END -=-" + Fore.RESET)


def test(tri, lst):
    return tri(list(lst))

# Messed up lists
any_numbers = random.sample(range(1, 1000), 5)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 15, 22, 23, 24, 32, 43, 51, 53, 56, 87, 99, 219]

inversed = [117, 90, 84, 81, 77, 67, 51, 50, 49, 42, 41, 34, 32, 21, 16, 8, 6, 4, 2, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 1, 9, 9, 9, 9, 0, 4, 4 ,4 ,4, 5, 4, 7, 1]

list_20 = [21, 24, 22, 25, 22, 26, 28, 28, 1, 4, 2, 5, 2, 6, 8, 8, 11, 14, 12, 15, 12, 16, 18, 18]


if __name__ == '__main__':
    get_most_efficient(list_20)


