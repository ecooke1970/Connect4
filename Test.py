from GameBoard import GameBoard


def main():
    test = GameBoard(rows=7, columns=6)

    test.print_board()

    print("Filling gameboard")
    letter = "a"
    for i in range(test.get_num_rows()):
        for j in range(test.get_num_columns()):
            test.set_position(letter, i, j)
            letter = chr(ord(letter) + 1)
            if letter == "{":
                letter = "A"
            # if letter == "Z":
            #   letter = "a"

    print("Printing gameboard")
    test.print_board()
    print("Printing row 1")
    print(test.get_row(1))
    print("Printing column 1")
    print(test.get_column(1))
    print("Printing diagonal from 5, 2")
    print(test.get_diagonal(5, 2))


if __name__ == "__main__":
    main()