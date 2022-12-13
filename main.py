from assist_functions import read_input, get_square, valid_moves, find_0, is_final, return_first_unmarked, beautify
from Node import Node
import colorama
import copy
import time


def dfs(input_state: list, show_work: bool = True):
    # initialize root node:
    pos_tup = find_0(input_state)
    current_node: Node = Node(input_state, x_pos=pos_tup[0], y_pos=pos_tup[1], follow_nodes=[], prev_node=None)
    current_node.set_mark(1)  # set as marked
    b = 0
    i = 0

    while not is_final(current_node.get_board()):  # while the current board still contains zeros
        i += 1
        if show_work:
            print(f'{colorama.Fore.GREEN} Branching from {current_node.get_pos()}:\n')
            print(beautify(current_node.get_board()))
            time.sleep(0.01)
        poss_vals = valid_moves(current_node.get_board(), current_node.get_pos())

        if poss_vals:  # if empty: back-track to previous node(s) that has one/multiple unvisited AND unmarked nodes
            for new_value in poss_vals:
                # modify the previous state accordingly:
                pos_tup = current_node.get_pos()
                new_state = copy.deepcopy(current_node.get_board())
                new_state[pos_tup[1]][pos_tup[0]] = new_value

                # construct new node out of the new state and append to stack
                try:
                    new_x_pos, new_y_pos = find_0(new_state)
                except TypeError:
                    beautify(current_node.get_board())
                new_node = Node(new_state, x_pos=new_x_pos, y_pos=new_y_pos, follow_nodes=[], prev_node=current_node)

                # add new neighbour-node to top of stack
                current_node.add_follow_node(new_node)

            # order the following nodes of current node, to decide what node to expand in the next iteration
            a = sorted(current_node.get_follow_nodes(), key=lambda x: len(valid_moves(x.get_board(), x.get_pos())))
            current_node.set_follow_nodes(a)

            # set new current node for next iteration if the node is unmarked:
            current_node = return_first_unmarked(current_node.get_follow_nodes())
            current_node.set_mark(1)

        else:  # branch has been explored and seems to lead to a dead end, backtrack:
            b += 1
            if show_work:
                print(
                    f'{colorama.Fore.RED}Backtrack from {current_node.get_pos()}:\n{beautify(current_node.get_board())}')
                time.sleep(0.01)
            while len([x for x in current_node.get_follow_nodes() if x.get_mark() == 0]) == 0:
                current_node = current_node.get_prev_node()
            current_node = return_first_unmarked(current_node.get_follow_nodes())
            current_node.set_mark(1)
    return f'Sudoku solved: \n {beautify(current_node.get_board())}'


if __name__ == "__main__":
    new_inp = read_input("C:\\Users\\Felix Unterleiter\\PycharmProjects\\pythonProject\\input.txt")
    print(dfs(input_state=new_inp, show_work=True))  # by adding the argument show_work=False to the dfs method, only the
    # solved sudoku will be displayed
