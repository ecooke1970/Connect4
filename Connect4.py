# Author: Erik Cooke

from GameBoard import GameBoard


def check_for_winner(board, player):
    # Check horizontally by row
    for i in range(board.get_num_rows()):
        if (player * 4) in board.get_row(i):
            return True

    # Check vertically by column
    for i in range(board.get_num_columns()):
        if (player * 4) in board.get_column(i):
            return True

    # Check diagonally every row first column up right and down right
    for i in range(board.get_num_rows()):
        if (player * 4) in board.get_diagonal(row=i, column=0, direction="dr"):
            return True
        if (player * 4) in board.get_diagonal(row=i, column=0, direction="ur"):
            return True

    # Check diagonally every column first row down right and every column last row up right
    for i in range(board.get_num_columns()):
        if (player * 4) in board.get_diagonal(row=0, column=i, direction="dr"):
            return True
        if (player * 4) in board.get_diagonal(row=board.get_num_rows() - 1, column=i, direction="ur"):
            return True

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
                self.moves += 1
                self.board.set_position(self.player, i, column)
                self.winner = check_for_winner(self.board, self.player)

                if not self.winner:
                    if self.player == 'X':
                        self.player = 'Y'
                    else:
                        self.player = 'X'

        self.board.print_board()
        print("Game Over")
        if self.player == "X":
            print("The winner is player 1")
        else:
            print("The winner is player 2")
