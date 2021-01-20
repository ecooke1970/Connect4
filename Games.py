# author: Erik Cooke

from Connect4 import Connect4


def print_menu():
    print("Games")
    print("\nEnter the number of your choice from the  menu")
    print("1. Connect 4")
    print("9. Exit")


def main():
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
