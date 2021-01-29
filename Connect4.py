# Author: Erik Cooke

from GameBoard import GameBoard
from tkinter import *
import tkinter as tk


class Connect4:
    def __init__(self):
        self.board = GameBoard(6, 7)
        self.player = 'X'
        self.moves = 0
        self.winner = False

    def play(self):
        print("play")

        def player_move(column):
            print("player_move executed")
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
                    self.winner = check_for_winner()

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
                window.update()

        def check_for_winner():
            print("check_for_winner")
            # Check horizontally by row
            for i in range(self.board.get_num_rows()):
                if (self.player * 4) in self.board.get_row(i):
                    return True

            # Check vertically by column
            for i in range(self.board.get_num_columns()):
                if (self.player * 4) in self.board.get_column(i):
                    return True

            # Check diagonally every row first column up right and down right
            for i in range(self.board.get_num_rows()):
                if (self.player * 4) in self.board.get_diagonal(row=i, column=0, direction="dr"):
                    return True
                if (self.player * 4) in self.board.get_diagonal(row=i, column=0, direction="ur"):
                    return True

            # Check diagonally every column first row down right and every column last row up right
            for i in range(self.board.get_num_columns()):
                if (self.player * 4) in self.board.get_diagonal(row=0, column=i, direction="dr"):
                    return True
                if (self.player * 4) in self.board.get_diagonal(row=self.board.get_num_rows() - 1, column=i,
                                                                direction="ur"):
                    return True

            return False

        print("\nWelcome to Connect 4")

        self.board.set_position('X', 2, 2)
        self.board.set_position('Y', 3, 2)
        self.board.set_position('X', 2, 6)
        self.board.set_position('Y', 5, 2)

        # while not self.winner:

        window = tk.Tk()
        window.title("Connect 4")

        top_frame = tk.Frame(window)
        my_btn1 = Button(top_frame, text="C1", command=lambda: player_move(1))
        my_btn2 = Button(top_frame, text="C2", command=lambda: player_move(2))
        my_btn3 = Button(top_frame, text="C3", command=lambda: player_move(3))
        my_btn4 = Button(top_frame, text="C4", command=lambda: player_move(4))
        my_btn5 = Button(top_frame, text="C5", command=lambda: player_move(5))
        my_btn6 = Button(top_frame, text="C6", command=lambda: player_move(6))
        my_btn7 = Button(top_frame, text="C7", command=lambda: player_move(7))
        top_frame.pack()
        my_btn1.grid(row=0, column=0)
        my_btn2.grid(row=0, column=1)
        my_btn3.grid(row=0, column=2)
        my_btn4.grid(row=0, column=3)
        my_btn5.grid(row=0, column=4)
        my_btn6.grid(row=0, column=5)
        my_btn7.grid(row=0, column=6)

        bottom_frame = tk.Frame(window)
        my_canvas = tk.Canvas(bottom_frame, bg="blue", height=700, width=800)

        x = 0
        y = 0
        for i in range(6):
            row = self.board.get_row(i, return_form="list")
            for col in row:
                if col == ' ':
                    my_canvas.create_oval(100 * x, 100 * y, x * 100 + 100, y * 100 + 100, fill="black")
                elif col == 'X':
                    my_canvas.create_oval(100 * x, 100 * y, x * 100 + 100, y * 100 + 100, fill="yellow")
                else:
                    my_canvas.create_oval(100 * x, 100 * y, x * 100 + 100, y * 100 + 100, fill="red")
                x += 1
            y += 1
            x = 0

        bottom_frame.pack(side="bottom")
        my_canvas.pack()

        window.mainloop()

        # print("Game Over")
        # if self.player == 'T':
        #     print("The game is a tie")
        # elif self.player == "X":
        #     print("The winner is player 1")
        # else:
        #     print("The winner is player 2")
