from board import Board


class Game:
    def __init__(self):
        self.board = Board()

    def start(self):
        print("Game started!")
        print(self.board)
        while True:
            # gen comp move
            print("Computer move: ")
            self.board.gen_computer_move()
            print(self.board)
            move_result = self.board.end_game()
            if move_result:
                print(move_result)
                break

            # get human move
            move = input("Your move: ")
            self.board.add_move(move)
            print(self.board)
            move_result = self.board.end_game()
            if move_result:
                print(move_result)
                break


if __name__ == '__main__':
    game = Game()
    game.start()
