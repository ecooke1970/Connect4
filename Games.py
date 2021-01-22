# author: Erik Cooke

from Connect4 import Connect4
import tkinter as tk


def print_menu():
    print("Games")
    print("\nEnter the number of your choice from the  menu")
    print("1. Connect 4")
    print("9. Exit")


def run_connect4():
    game = Connect4()
    game.play()


def main():
    window = tk.Tk()
    window.title("Games Menu")

    top_frame = tk.Frame(window).pack()
    bottom_frame = tk.Frame(window).pack(side="bottom")
    btn1 = tk.Button(top_frame, text="Connect 4", fg="green", command=run_connect4)
    btn2 = tk.Button(bottom_frame, text="Exit", fg="red")
    btn1.pack()
    btn2.pack()

    window.mainloop()

    print_menu()

    user_choice = int(input("Your selection: "))

    while user_choice != 9:
        if user_choice == 1:
            game = Connect4()
            game.play()

        print_menu()
        user_choice = int(input("Your selection: "))


if __name__ == "__main__":
    main()
