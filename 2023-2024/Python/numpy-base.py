"""
Bases de - ARAUJO José
TG4
"""
import numpy as np

# tab = np.array([1, 1.5, 2, 2.5])
# tab2 = 2*tab # Il va mult chaque valeur 
# print(tab2)

# L = [1, 1.5, 2, 2.5] 
# L2 = 2*L # Il va multi la liste
# print(L2)


# tab1 = np.linspace(0, 10, 5)
# print(tab1)

# # Exercice 6



# compteur1 = 0
# compteur2 = 2
# for i in range(100000):
#     tab3=np.random.rand(10)*6.0+4.0
#     for x in tab3:
#         if 4.00 < x < 4.002:
#             compteur1 = compteur1 + 1
#             if 9.998 < x < 9.999:
#                 compteur2 = compteur2 + 1
# print("Compteur 1:", compteur1)
# print("Compteur 2:", compteur2)


# Exercice fin

"""
2x - 3y + 1z = -8
x + y + z = 3
3x - y + z = -1
"""

a = np.array([[2, -3, 1], [1, 1, 1], [3, -1, 1]])
e = np.array([[-8], [3], [-1]])
b = np.linalg.inv(a)
x = np.dot(b, e)
print(x)