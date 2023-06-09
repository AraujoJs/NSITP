
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

def get_piece(liste, j, i):
    piece = liste[j][i]
    if (piece == 1):
        return "X"
    elif (piece == 2):
        return "O"
    elif (piece == 3):
        return "R"
    else:
        return " "

def draw(isBegin=False):
    line = ""
    print("   A    B    C    D    E   ")
    print("-" * 26)
    for j in range(5):
        for i in range(5):
            piece = ""
            if(isBegin):
                piece = get_piece(init, j + 1, i + 1)
            else:
                piece = get_piece(plateau, j + 1, i + 1)
            line += f"| {piece:2} "
        print(f"{j + 1}" + line + "|")
        print("-" * 26)
        line = ""

def verify_at(case):
    return plateau[case[0] - 1][case[1] - 1] == 0


def get_cases_valid(roi_position=(3, 3)):
    x = roi_position[0]
    y = roi_position[1]
    cases = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            case = (roi_position[0] - i, roi_position[1] - j)
            free = verify_at(case)
            if case != roi_position and free:
                cases.append(case)

    print(cases)
            

def roi_valide(mov, roi_position):
    moves =  [1, 2, 3, 4, 6, 7, 8, 9]
    if (mov in moves):
        cases_valides = get_cases_valid(roi_position)



def get_mov(message):
    if (len(message) == 3):
        pion = message[0:2]
        direc = message[-1]
        roi = 0
    
    elif (len(message) == 4):
        roi = message[0]
        pion = message[1:3]
        direc = message[-1]

    
    is_roi_valid = roi_valide(roi, (3, 3))



draw()

message = str(input("Jouez un coup [sous la forme: D28]:"))

get_cases_valid((3, 3))
