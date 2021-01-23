# Author: Erik Cooke

from GameBoard import GameBoard
# from tkinter import *
import tkinter as tk


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


def draw_board():
    board = tk.Tk()
    board.title("Connect 4")

    top_frame = tk.Frame(board)
    my_btn1 = tk.Button(top_frame, text="C1")
    my_btn2 = tk.Button(top_frame, text="C2")
    my_btn3 = tk.Button(top_frame, text="C3")
    my_btn4 = tk.Button(top_frame, text="C4")
    my_btn5 = tk.Button(top_frame, text="C5")
    my_btn6 = tk.Button(top_frame, text="C6")
    my_btn7 = tk.Button(top_frame, text="C7")
    top_frame.pack()
    my_btn1.grid(row=0, column=0)
    my_btn2.grid(row=0, column=1)
    my_btn3.grid(row=0, column=2)
    my_btn4.grid(row=0, column=3)
    my_btn5.grid(row=0, column=4)
    my_btn6.grid(row=0, column=5)
    my_btn7.grid(row=0, column=6)

    bottom_frame = tk.Frame(board)
    my_canvas = tk.Canvas(bottom_frame, bg="blue", height=500, width=500)
    my_canvas.create_oval(0, 0, 100, 100, fill="red")
    bottom_frame.pack(side="bottom")
    my_canvas.grid()

    board.mainloop()


class Connect4:
    def __init__(self):
        self.board = GameBoard(6, 7)
        self.player = 'X'
        self.moves = 0
        self.winner = False

    def play(self):
        print("\nWelcome to Connect 4")

        draw_board()

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
                if self.moves > 6:
                    self.winner = check_for_winner(self.board, self.player)

                # if no winner, check if board is full, if not switch players
                if not self.winner:
                    if self.moves > 41:
                        self.player = 'T'
                        self.winner = True
                    elif self.player == 'X':
                        self.player = 'Y'
                    else:
                        self.player = 'X'

        self.board.print_board()
        print("Game Over")
        if self.player == 'T':
            print("The game is a tie")
        elif self.player == "X":
            print("The winner is player 1")
        else:
            print("The winner is player 2")
