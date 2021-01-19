# Connect 4 game
# Authors: Erik Cooke, Chazz M, Jace C
from GameBoard import GameBoard
import pygame
import math
import time
import tkinter as tk

#Color Variables
BLUE = (0,0,255)
BLACK = (0,0,0)
RED =(255,0,0)
YELLOW = (255,255,0)

def check_for_winner(board, player):
    """Checks the board 2d list for a 4 in the row winner"""

    # check horizontally by row
    for row in range(6):
        test = ""
        test_list = board.get_row(row)
        for x in test_list:
            test += x
        if (player * 4) in test:
            return True

    # check vertically by column
    for col in range(7):
        test = ""
        test_list = board.get_column(col)
        for x in test_list:
            test += x
        if (player * 4) in test:
            return True

    # check diagonally	
    j = 0
    for i in range(3, 5):
        test = ""
        test_list = board.get_diagonal(i, j)
        for x in test_list:
            test += x
        if (player * 4) in test:
            return True
    j = 5
    for i in range(4):
        test = ""
        test_list = board.get_diagonal(j, i)
        for x in test_list:
            test += x
        if (player * 4) in test:
            return True

    j = 0
    for i in range(4):
        test = ""
        test_list = board.get_diagonal(j, i, direction="down")
        for x in test_list:
            test += x
        if (player * 4) in test:
            return True

    j = 0
    for i in range(1, 3):
        test = ""
        test_list = board.get_diagonal(i, j, direction="down")
        for x in test_list:
            test += x
        if (player * 4) in test:
            return True

    return False
# Function creates board using various shape
def draw_board(board, screen, blockSize):
    """Draws the gameboard based on the contents of board"""
    
    radius = int(blockSize/2 - 5)
    
    for col in range(7):
        for row in range(6):
            pygame.draw.rect(screen, BLUE, (col*blockSize, row*blockSize + blockSize, blockSize, blockSize))
            pygame.draw.circle(screen, BLACK, (int(col*blockSize+blockSize/2), int(row*blockSize + blockSize +
            blockSize/2)),radius)
            
    for col in range(7):
        for row in range(6):
            if board.get_position(row, col) == "X":
                pygame.draw.circle(screen, RED, (int(col*blockSize+blockSize/2), int(row*blockSize + blockSize +
                blockSize/2)),radius)
            elif board.get_position(row, col) == "Y":
                pygame.draw.circle(screen, YELLOW, (int(col*blockSize+blockSize/2), int(row*blockSize + blockSize +
                blockSize/2)),radius)
        pygame.display.update()

def intro_prompt():
    """Displays the game introduction with rules"""
    root = tk.Tk()

    """ using root.geometry to find the center of the screen so the tkinter window displays there"""
    w = 400
    h = 200

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.wm_title("Welcome to Connect Four!")
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    introPrompt = tk.Canvas(root, width = w, height = h, bg = 'black')
    introPrompt.pack()

    label1 = tk.Label (root, text = "\nWelcome to Connect Four! The object of the game is to get"  +
                                    "\nfour of your pieces in a row horizontally, vertically, or"  +
                                    "\ndiagonally, while at the same time blocking your opponent.",
                                    bg = 'black', fg = 'white')
    
    label1.config(font=('helvetica', 10, 'bold'))
    introPrompt.create_window(200, 75, window = label1)

    """ if the "play again!" button is clicked, the tkinter window is closed"""
    """and the main function is called to run the program again"""
    def start_game():
        root.destroy()
    def close_game():
        root.destroy()
        pygame.quit()
        
    button1 = tk.Button(root, text = "Let's play!", command = start_game, bg = 'green', fg = 'white')
    button2 = tk.Button(root, text = "Exit", command = close_game, bg = 'brown', fg = 'white')
    introPrompt.create_window(150, 150, window = button1)
    introPrompt.create_window(250, 150, window = button2)

    root.mainloop()
        
def play_again_prompt():
    """Displays a windows asking the user if they want to play another game or exit"""
    
    root = tk.Tk()

    #using root.geometry to find the center of the screen so the tkinter window displays there
    w = 220
    h = 100

    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    root.wm_title("Play Again?")
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    playPrompt = tk.Canvas(root, width = w, height = h, bg = 'black')
    playPrompt.pack()

    label1 = tk.Label (root, text = "Would you like to play again?", bg = 'black', fg = 'white')
    label1.config(font=('helvetica', 10, 'bold'))
    playPrompt.create_window(110, 25, window = label1)

    # if the "play again!" button is clicked, the tkinter window is closed
    # and the main function is called to run the program again
    def restart_game():
        empty_board_sound.play()
        root.destroy()
        main()
    def close_game():
        root.destroy()
        pygame.quit()
    button1 = tk.Button(root, text = "Play again!", command = restart_game, bg = 'blue', fg = 'white')
    button2 = tk.Button(root, text = "Exit", command = close_game, bg = 'brown', fg = 'white')
    playPrompt.create_window(65, 60, window = button1)
    playPrompt.create_window(175, 60, window = button2)

    root.mainloop()

def drop_piece(board, col, row, player, screen, blockSize):
    """Animates a game piece dropping into the game board"""
    for i in range(row):
        board.set_position(player, i, col)
        draw_board(board, screen, blockSize)
        pygame.display.update()
        time.sleep(.05)
        board.set_position(' ', i, col)

def main():
    """Variables"""
    """GameBoard object used to store the board"""
    board = GameBoard(6,7)

    """ keeps track of which player is going"""
    player = "X"
    moves = 0
    global empty_board_sound

    pygame.init()
    pygame.mixer.init()
    
    """ Sound for dropping game pieces"""
    drop_sound = pygame.mixer.Sound('drop_01.wav')
    """ Sound for emptying the game board"""    
    empty_board_sound = pygame.mixer.Sound('empty_board.wav')
    
    blockSize = 100
    width =  7 * blockSize
    height = (6 + 1) * blockSize

    size = (width, height)
    radius = int(blockSize/2 - 5)
    
    screen = pygame.display.set_mode(size)
    draw_board(board, screen, blockSize)
    pygame.display.set_caption('Connect Four')
    pygame.display.update()
    
    pygame.font.init()
    myfont = pygame.font.SysFont("monospace", 75)
    winner = False
    intro_prompt()
    
    """Main game loop"""
    while not winner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winner = True
                pygame.quit()
                
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0,0, width, blockSize))
                posx = event.pos[0]

                if player == 'X':
                    pygame.draw.circle(screen, RED, (posx, int(blockSize/2)), radius)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(blockSize/2)), radius)
            pygame.display.update()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0,0, width, blockSize))
                
                posx = event.pos[0]
                """using math.floor, the coordinates of where the player clicks on the board can be divided by 100
                       into more usable single integers. Instead of pos (650,240) you have column 6, row 2"""
                    
                col = int(math.floor(posx/blockSize))
                
                valid_move = False
                place_found = False
                i = 5
                while not place_found:
                    if i < 0:
                        place_found = True
                    elif board.get_position(i, col) == ' ':
                        place_found = True
                        valid_move = True
                    else:
                        i -= 1
                    
                if valid_move:
                    
                    moves += 1
                    drop_sound.play()                    
                    drop_piece(board, col, i, player, screen, blockSize)
                    board.set_position(player, i, col)
                    pygame.display.update()     
                    draw_board(board, screen, blockSize)

                    winner = check_for_winner(board, player)
                    
                    """displays winner above board"""
                    if winner:
                        if player == "Y":
                            winlabel = myfont.render("Player 2 wins!", 1, YELLOW)
                            screen.blit(winlabel, (40,10))
                            pygame.display.update()
                            play_again_prompt()                            
                            
                        else:
                            winlabel = myfont.render("Player 1 wins!", 1, RED)
                            screen.blit(winlabel, (40,10))
                            pygame.display.update()
                            play_again_prompt()
                            
                    if moves >= 42:
                        winlabel = myfont.render("Tie Game", 1, BLUE)
                        screen.blit(winlabel, (40,10))
                        pygame.display.update()
                        play_again_prompt()
                            
                            
                    if player == "X":
                        player = "Y"
                    else:
                        player = "X"

if __name__ == "__main__":
    main()
