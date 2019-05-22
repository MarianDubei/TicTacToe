from btree import LinkedBinaryTree
import random
import copy


class Board:
    COMPUTER_SIGN = "O"
    HUMAN_SIGN = "X"

    def __init__(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        # self.board = [['X', 'O', 'X'], ['O', 'X', 'X'], ['O', ' ', 'O']]
        self.last_move = None

    def add_move(self, move):
        moves_dct = {"1": (0, 0), "2": (0, 1), "3": (0, 2),
                     "4": (1, 0), "5": (1, 1), "6": (1, 2),
                     "7": (2,0), "8": (2, 1), "9": (2, 2)}
        last_move_r = moves_dct[move][0]
        last_move_c = moves_dct[move][1]
        self.board[last_move_r][last_move_c] = Board.HUMAN_SIGN

    @staticmethod
    def get_empties(board):
        empties = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    empties.append((i, j))
        return empties

    @staticmethod
    def get_result(board):
        lines = []
        for i in range(3):
            lines.append(list(set(board[i])))
            lines.append(list(set([w[0] for w in board])))
        lines.append(list(set([board[i][i] for i in range(3)])))
        lines.append(list(set([board[i][2 - i] for i in range(3)])))
        for line in lines:
            if len(line) == 1:
                if line[0] == " ":
                    continue
                elif line[0] == Board.COMPUTER_SIGN:
                    return 1
                else:
                    return -1
        if not Board.get_empties(board):
            return 0
        return 2

    @staticmethod
    def get_points(tree):
        points = 0

        def res_recurse(tree, points):
            board = tree.key
            board_result = Board.get_result(board)
            if board_result == 2:
                points += res_recurse(tree.left, points)
                points += res_recurse(tree.right, points)
                return points
            else:
                points += board_result
                return points
        return res_recurse(tree, points)

    def build_tree(self):
        tree = LinkedBinaryTree(self.board)

        def recurse(board, tree, prev_move):
            empties = Board.get_empties(board)
            if len(empties) == 1:
                pos = empties[0]
                board1 = copy.deepcopy(board)
                board1[pos[0]][pos[1]] = Board.HUMAN_SIGN
                board2 = copy.deepcopy(board)
                board2[pos[0]][pos[1]] = Board.HUMAN_SIGN
                tree.insert_left(board1)
                tree.insert_right(board2)
                return
            else:
                pos1 = random.choice(empties)
                empties.remove(pos1)
                pos2 = random.choice(empties)
                board1 = copy.deepcopy(board)
                board2 = copy.deepcopy(board)
                if prev_move == Board.COMPUTER_SIGN:
                    curr_move = Board.HUMAN_SIGN
                else:
                    curr_move = Board.COMPUTER_SIGN
                board1[pos1[0]][pos1[1]] = curr_move
                board2[pos2[0]][pos2[1]] = curr_move
                tree.insert_left(board1)
                tree.insert_right(board2)
                recurse(board1, tree.get_left(), curr_move)
                recurse(board2, tree.get_right(), curr_move)

        recurse(self.board, tree, Board.HUMAN_SIGN)

        points_left = Board.get_points(tree.left)
        points_right = Board.get_points(tree.right)
        if points_left > points_right:
            return tree.left.key
        else:
            return tree.right.key

    def gen_computer_move(self):
        tree = self.build_tree()
        self.board = tree

    def end_game(self):
        result = Board.get_result(self.board)
        if result == 1:
            return "Computer won."
        elif result == -1:
            return "Human won."
        elif result == 0:
            return "Draw."
        else:
            return False

    def __str__(self):
        board_str = []
        sups = [u"\u00B9", u"\u00B2", u"\u00B3", u"\u2074", u"\u2075",
                u"\u2076", u"\u2077", u"\u2078", u"\u2079"]
        for i in range(len(self.board)):
            high_str = f"  {sups[i*3]}|  {sups[i*3+1]}|  {sups[i*3+2]}\n"
            mid_str = f" {self.board[i][0]} | {self.board[i][1]} | {self.board[i][2]}\n"
            board_str.append(high_str + mid_str)
        board_str = "___|___|___\n".join(board_str)
        board_str += "   |   |"
        return board_str


if __name__ == '__main__':
    board = Board()
    print(board)
    print(board.get_result(board.board))
