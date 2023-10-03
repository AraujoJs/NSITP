"""
"""
prix_billet_joseph = 0
n_billet = 0
n_prix = 0

def init():
    global prix_billet_joseph, n_billet, n_prix
    prix_billet_joseph = int(input())
    n_billet = int(input())
    n_prix = input().split(" ")

def verifier_prix(prix_joseph, n_billet, n_prix):
    count = 0
    for i in range(n_billet):
        if int(n_prix[i]) < prix_joseph:
            count += 1
    if count >= 3:
        print(" ARNAQUE ! ")
    else:
        print(" Ok bon voyage, bisous, n'oublie pas de m'envoyer des photos ! ")

if __name__ == "__main__":
    init()
    verifier_prix(prix_billet_joseph, n_billet, n_prix)
    


