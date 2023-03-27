import random
from tri import tri_selection, tri_bulles, tri_insertion, tri_insertion_2, tri_insertion_3


def get_most_efficient(list):
    most_efficient = None

    print("-=-"*5 + "MOST EFFICENT" + "-=-" *5)
    print("tri selection:")
    dic = test(tri_selection, list)
    comp_selection = dic["comp"]
    echange_selection = dic["echange"]
    print(dic["list"])
    print(f"N° comparaison: {comp_selection} \nN° d'echange: {echange_selection}\n")

    print("tri bubble:")
    dic = test(tri_bulles, list)
    comp_bubble = dic["comp"]
    echange_bubble = dic["echange"]
    print(dic["list"])
    print(f"N° comparaison: {comp_bubble} \nN° d'echange: {echange_bubble}\n")

    print("tri insertion[case 1]:")
    dic = test(tri_insertion, list)
    comp_insert = dic["comp"]
    echange_insert = dic["echange"]
    print(dic["list"])
    print(f"N° comparaison: {comp_insert} \nN° d'echange: {echange_insert}\n")

    print("tri insertion[case 2]:")
    dic = test(tri_insertion_2, list)
    comp_insert_2 = dic['comp']
    echange_insert_2 = dic['echange']
    print(dic["list"])
    print(f"N° comparaison: {comp_insert_2} \nN° d'echange: {echange_insert_2}\n")

    print("tri insertion[case 3]:")
    dic = test(tri_insertion_3, list)
    comp_insert_3 = dic['comp']
    echange_insert_3 = dic["echange"]
    print(dic['list'])
    print(f"N° comparaison: {comp_insert_3} \nN° d'echange: {echange_insert_3}\n")

    print("—=- MOST EFICIENT:")
    


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


