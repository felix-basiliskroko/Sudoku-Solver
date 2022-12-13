# Class: Node, where each node will represent a board-state
class Node:
    def __init__(self, board_state: list, x_pos: int, y_pos: int, follow_nodes: list, prev_node, mark: int = 0):
        self.board_state = board_state
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.follow_nodes = follow_nodes
        self.prev_node = prev_node
        self.mark = mark

    def get_pos(self):
        return self.x_pos, self.y_pos

    def get_board(self):
        return self.board_state

    def get_follow_nodes(self):
        return self.follow_nodes

    def get_mark(self):
        return self.mark

    def get_prev_node(self):
        return self.prev_node

    def add_follow_node(self, n):
        self.follow_nodes.append(n)

    def set_follow_nodes(self, li: list):
        self.follow_nodes = li

    def set_mark(self, m):
        if m == 0 or m == 1:
            self.mark = m
        else:
            raise ValueError(f'The mark for a node can only be 0 or 1, not {m}')
