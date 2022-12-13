import os


def read_input(path):  # provide global path here
    lis = []
    bullshit_counter = 0

    file_name = path.split("\\")[-1]
    path_name = path.split("\\")[:-1]
    path_name = '\\'.join(path_name)

    os.chdir(path_name)
    with open(file_name, 'r') as f:
        i = f.readlines()

    for row in i:
        if bullshit_counter <= 7:
            row = row[:-1]  # remove '\n'
            x = [int(number) for number in row]  # row-column
            lis.append(x)
            bullshit_counter += 1
        else:
            break

    lis.append([int(el) for el in i[-1]])
    return lis


# gigantic method to satisfy requirement of only one identical number in each box lol
def get_square(board: list, x: int, y: int):
    out = []
    if x < 3 and y < 3:
        for y_ax in range(0, 3):
            for x_ax in range(0, 3):
                out.append(board[y_ax][x_ax])

    if x < 3 <= y < 6:
        for y_ax in range(3, 6):
            for x_ax in range(0, 3):
                out.append(board[y_ax][x_ax])

    if x < 3 and 9 > y >= 6:
        for y_ax in range(6, 9):
            for x_ax in range(0, 3):
                out.append(board[y_ax][x_ax])

    if 6 > x >= 3 > y:
        for y_ax in range(0, 3):
            for x_ax in range(3, 6):
                out.append(board[y_ax][x_ax])

    if 6 > x >= 3 and 6 > y >= 3:
        for y_ax in range(3, 6):
            for x_ax in range(3, 6):
                out.append(board[y_ax][x_ax])
    if 3 <= x < 6 <= y < 9:
        for y_ax in range(6, 9):
            for x_ax in range(3, 6):
                out.append(board[y_ax][x_ax])
    if 9 > x >= 6 and y < 3:
        for y_ax in range(0, 3):
            for x_ax in range(6, 9):
                out.append(board[y_ax][x_ax])
    if 9 > x >= 6 > y >= 3:
        for y_ax in range(3, 6):
            for x_ax in range(6, 9):
                out.append(board[y_ax][x_ax])

    if 9 > x >= 6 and 9 > y >= 6:
        for y_ax in range(6, 9):
            for x_ax in range(6, 9):
                out.append(board[y_ax][x_ax])

    return out


def valid_moves(board: list, field: tuple):
    possible_values = [i for i in range(1, 10)]

    # check for column
    col = [x[field[0]] for x in board]
    possible_values = [a for a in possible_values if a not in col]

    # check for row
    row = board[field[1]]
    possible_values = [a for a in possible_values if a not in row]

    # check for box
    box = get_square(board, field[0], field[1])
    possible_values = [a for a in possible_values if a not in box]

    return possible_values


# finds first 0 in provided board
def find_0(board: list):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return col, row


# checks if the board is solved
def is_final(board: list):
    for row in board:
        if 0 in row:
            return False
    return True


# returns the first node that is marked as unvisited
def return_first_unmarked(follow_nodes: list):
    for node in follow_nodes:
        if node.get_mark() == 0:
            return node
    return None


# for output
def beautify(board: list):
    b0_0, b0_1, b0_2 = board[0][:3], board[0][3:6], board[0][6:9]
    b1_0, b1_1, b1_2 = board[1][:3], board[1][3:6], board[1][6:9]
    b2_0, b2_1, b2_2 = board[2][:3], board[2][3:6], board[2][6:9]
    b3_0, b3_1, b3_2 = board[3][:3], board[3][3:6], board[3][6:9]
    b4_0, b4_1, b4_2 = board[4][:3], board[4][3:6], board[4][6:9]
    b5_0, b5_1, b5_2 = board[5][:3], board[5][3:6], board[5][6:9]
    b6_0, b6_1, b6_2 = board[6][:3], board[6][3:6], board[6][6:9]
    b7_0, b7_1, b7_2 = board[7][:3], board[7][3:6], board[7][6:9]
    b8_0, b8_1, b8_2 = board[8][:3], board[8][3:6], board[8][6:9]

    return f'_________________________________\n| {b0_0} {b0_1} {b0_2} |\n| {b1_0} {b1_1} {b1_2} |\n| {b2_0} {b2_1} {b2_2} |\n_________________________________\n| {b3_0} {b3_1} {b3_2} |\n| {b4_0} {b4_1} {b4_2} |\n| {b5_0} {b5_1} {b5_2} |\n_________________________________\n| {b6_0} {b6_1} {b6_2} |\n| {b7_0} {b7_1} {b7_2} |\n| {b8_0} {b8_1} {b8_2} |\n_________________________________\n '
