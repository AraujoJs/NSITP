# ---- DONNÉES ----

init = [
    [9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 9],
    [9, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 3, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 9],
    [9, 2, 2, 2, 2, 2, 9],
    [9, 9, 9, 9, 9, 9, 9],
]

plateau = [
    [9, 9, 9, 9, 9, 9, 9],
    [9, 1, 1, 1, 1, 1, 9],
    [9, 0, 0, 0, 0, 0, 9],
    [9, 0, 0, 3, 0, 0, 9],
    [9, 0, 0, 0, 0, 0, 9],
    [9, 2, 2, 2, 2, 2, 9],
    [9, 9, 9, 9, 9, 9, 9],
]

fini = False
premier_mov = True
x_de_jouer = True


roi_position = (3, 3)
pion_position = (0,0)
pion_case = (0, 0)


# ---- ROI ET PION ----

def roi_est_valide(mouvement):
    mouvements = ["1", "2", "3", "4", "6", "7", "8", "9"]
    case = (0, 0)
    if mouvement in mouvements:
        cases_dispo = verifier_cases_valides_roi(roi_position)
        if mouvement == "1":
            case = cases_dispo[5]
        elif mouvement == "2":
            case = cases_dispo[3]
        elif mouvement == "3":
            case = cases_dispo[0]
        elif mouvement == "4":
            case = cases_dispo[6]
        elif mouvement == "6":
            case = cases_dispo[1]
        elif mouvement == "7":
            case = cases_dispo[7]
        elif mouvement == "8":
            case = cases_dispo[4]
        elif mouvement == "9":
            case = cases_dispo[2]
    return case

def pion_est_valide(pion_position, direction):
    directions = ["1", "2", "3", "4", "6", "7", "8", "9"]
    if direction in directions:
        nouvelle_case: tuple = case_mouvement_pion(pion_position, direction)
        if direction == "1":
            pion_position = nouvelle_case
        elif direction == "2":
            pion_position = nouvelle_case
        elif direction == "3":
            pion_position = nouvelle_case
        elif direction == "4":
            pion_position = nouvelle_case
        elif direction == "6":
            pion_position = nouvelle_case
        elif direction == "7":
            pion_position = nouvelle_case
        elif direction == "8":
            pion_position = nouvelle_case
        elif direction == "9":
            pion_position = nouvelle_case
    else:
        pion_position = (0, 0)
    return pion_position

def deplacer_roi(roi_pos, nouvelle_pos):
    global roi_position
    plateau[roi_pos[1]][roi_pos[0]], plateau[nouvelle_pos[1]][nouvelle_pos[0]] = \
        plateau[nouvelle_pos[1]][nouvelle_pos[0]], plateau[roi_pos[1]][roi_pos[0]]
    roi_position = nouvelle_pos

def deplacer_pion(pion_pos, nouvelle_pos):
    global pion_position
    plateau[pion_pos[0]][pion_pos[1]], plateau[nouvelle_pos[0]][nouvelle_pos[1]] = \
    plateau[nouvelle_pos[0]][nouvelle_pos[1]], plateau[pion_pos[0]][pion_pos[1]]
    pion_position = nouvelle_pos

def verifier_cases_valides_roi(roi_pos):
    cases = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            case = (roi_pos[0] - i, roi_pos[1] - j)
            free = case_est_libre(case)
            if free:
                cases.append(case)
            elif case != roi_pos:
                cases.append((0,0))
    return cases

def verifier_cases_valides_pion(pion):
    cases = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            case = (pion[0] - i, pion[1] - j)
            free = case_est_libre(case)
            if free:
                cases.append(case)
            else:
                cases.append((0,0))
    return cases

def case_mouvement_pion(pion, direction):
    derniere_position = (0, 0)
    disponible = False

    if direction == "1":
        derniere_position = (pion[0] + 1, pion[1] - 1)
        disponible = case_est_libre(derniere_position)

    elif direction == "2":
        derniere_position = (pion[0] + 1, pion[1])
        disponible = case_est_libre(derniere_position)

    elif direction == "3":
        derniere_position = (pion[0] + 1, pion[1] + 1)
        disponible = case_est_libre(derniere_position)

    elif direction == "4":
        derniere_position = (pion[0], pion[1] - 1)
        disponible = case_est_libre(derniere_position)

    elif direction == "6":
        derniere_position = (pion[0], pion[1] + 1)
        disponible = case_est_libre(derniere_position)

    elif direction == "7":
        derniere_position = (pion[0] - 1, pion[1] - 1)
        disponible = case_est_libre(derniere_position)

    elif direction == "8":
        derniere_position = (pion[0] - 1, pion[1])
        disponible = case_est_libre(derniere_position)

    elif direction == "9":
        derniere_position = (pion[0] - 1, pion[1] + 1)
        disponible = case_est_libre(derniere_position)

    if disponible:
        return case_mouvement_pion(derniere_position, direction)
    else:
        return pion

def effectuer_mouvements(roi, pion, roi_mov, pion_mov):
    global premier_mov

    roi_position = roi
    pion_position = pion

    pion_case = pion_est_valide(pion, pion_mov)
    roi_case = roi_est_valide(roi_mov)

    if premier_mov:
        if pion_case == (0, 0):
            print("Mouvement interdit!")
        elif pion_case == pion_position:
            print("Case occupée!")
        else:
            deplacer_pion(pion_position, pion_case)
            premier_mov = False
    else:
        if pion_case == (0,0) or roi_case == (0, 0):
            print("Mouvement interdit, ressayez!")
            return False
        else:
            deplacer_roi(roi_position, roi_case)
            deplacer_pion(pion_position, pion_case)
    return True


def case_est_libre(case):
    return plateau[case[0]][case[1]] == 0

# ---- TABLEAU ----
def dessiner_plateau(premiere_fois=False):
    ligne = ""
    print("   A    B    C    D    E   ")
    print("-" * 26)
    for j in range(5):
        for i in range(5):
            if premiere_fois:
                piece = prendre_piece(init, j + 1, i + 1)
            else:
                piece = prendre_piece(plateau, j + 1, i + 1)

            ligne += f"| {piece:2} "
        if j == 1:
            print(f"{j + 1}" + ligne + "|     <7    8   9>")
        elif j == 2:
            print(f"{j + 1}" + ligne + "|     <4        6>")
        elif j == 3:
            print(f"{j + 1}" + ligne + "|     <1   2    3>")
        else:
            print(f"{j + 1}" + ligne + "|")
        print("-" * 26)
        ligne = ""

def prendre_piece(table, j, i):
    piece = table[j][i]
    if piece == 1:
        return "X"
    elif piece == 2:
        return "O"
    elif piece == 3:
        return "R"
    else:
        return " "


def demander_user(player, premiere_fois):
    global fini
    if premiere_fois:
        reponse = str(input(f"Jouez le premier mouvement pour {player} [ex. -> A12]: "))
    else:
        reponse = str(input(f"Jouez le un mouvement pour {player} [ex. -> 2A12]: "))
    return reponse

# ---- INPUT ----
def game_loop():
    global fini, x_de_jouer, pion_position
    while not fini:
        movements = ""
        if premier_mov:
            while len(movements) != 3:
                if x_de_jouer:
                    movements = demander_user("X", True)
                else:
                    movements = demander_user("O", True)
        else:
            while len(movements) != 4:
                if x_de_jouer:
                    movements = demander_user("X", False)
                else:
                    movements = demander_user("O", False)


        index = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

        if premier_mov:
            pion = movements[0:2]
            pion_mov = movements[-1]
            roi_mov = 0

        else:
            pion = movements[1:3]
            pion_mov = movements[-1]
            roi_mov = movements[0]


        pion_position = (int(pion[1]), index[pion[0]])

        free = case_est_libre(pion_position)

        if free:
            print("Mouvement invalide!")

        else:
            cases = verifier_cases_valides_pion(pion_position)
            if cases.count((0,0)) == len(cases):
                fini = True

            if fini:
                if x_de_jouer:
                    fini_game("O")
                else:
                    fini_game("X")
            else:
                success = effectuer_mouvements(roi_position, pion_position, roi_mov, pion_mov)
                if success:
                    if x_de_jouer:
                        x_de_jouer = False
                    else:
                        x_de_jouer = True
                dessiner_plateau()


def input_valid(lance):
    if (premier_mov and len(lance) == 3) or (not premier_mov and len(lance) == 4):
        return True
    else:
        return False

def fini_game(joueur):
    print(f"Joueur {joueur} a gagné!")
# ---- INITIALISATION ----

if __name__ == "__main__":
    dessiner_plateau(True)
    game_loop()