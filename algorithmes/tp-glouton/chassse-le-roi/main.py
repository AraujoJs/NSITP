
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

def get_piece(j, i):
    piece = init[j][i]
    if (piece == 1):
        return "X"
    elif (piece == 2):
        return "O"
    elif (piece == 3):
        return "R"
    else:
        return " "

def draw():
    a = "0"
    line = ""
    print("   A    B    C    D    E   ")
    print("-" * 26)
    for j in range(5):
        for i in range(5):
            piece = get_piece(j + 1, i + 1)
            line += f"| {piece:2} "
        print(f"{j + 1}" + line + "|")
        line = ""
    print("-" * 26)

draw()