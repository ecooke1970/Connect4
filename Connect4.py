# Author: Erik Cooke

from GameBoard import GameBoard


def check_for_winner():
    return False


class Connect4:
    def __init__(self):
        self.board = GameBoard(6, 7)
        self.player = 'X'
        self.moves = 0
        self.winner = False

    def play(self):
        print("Welcome to Connect 4")

        while not self.winner:
            self.board.print_board()
            if self.player == 'X':
                column = int(input("Player 1 choose a column: "))
            else:
                column = int(input("Player 2 choose a column: "))

            column -= 1

            valid_move = False
            place_found = False
            i = 5
            while not place_found:
                if i < 0:
                    place_found = True
                elif self.board.get_position(i, column) == ' ':
                    place_found = True
                    valid_move = True
                else:
                    i -= 1

            if valid_move:
                self.board.set_position(self.player, i, column)
                self.winner = check_for_winner()
                self.moves += 1

                if self.player == 'X':
                    self.player = 'Y'
                else:
                    self.player = 'X'

        print("Game Over")
