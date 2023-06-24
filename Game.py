"""

made by
  _____     _                        _    _           _       
 |_   _|   | |                      | |  | |         (_)      
   | |  ___| |__  _ __ __ _  __ _   | |__| | __ _ ___ _ _ __  
   | | / __| '_ \| '__/ _` |/ _` |  |  __  |/ _` / __| | '_ \ 
  _| |_\__ \ | | | | | (_| | (_| |  | |  | | (_| \__ \ | | | |
 |_____|___/_| |_|_|  \__,_|\__, |  |_|  |_|\__,_|___/_|_| |_|
                               | |                           
                               |_|                           
                               
"""
# Import pygame, sys and numpy libraries
import pygame
import sys
import numpy as np

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Create the screen object
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the title of the screen
pygame.display.set_caption("Tic Tac Toe")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define the board size and the cell size
BOARD_ROWS = 3
BOARD_COLS = 3
CELL_SIZE = 200

# Define the board as a 3x3 numpy array of zeros
board = np.zeros((BOARD_ROWS, BOARD_COLS))

# Define a function to draw the lines on the screen
def draw_lines():
    # Draw the horizontal lines
    pygame.draw.line(screen, BLACK, (0, CELL_SIZE), (SCREEN_WIDTH, CELL_SIZE), 10)
    pygame.draw.line(screen, BLACK, (0, 2 * CELL_SIZE), (SCREEN_WIDTH, 2 * CELL_SIZE), 10)

    # Draw the vertical lines
    pygame.draw.line(screen, BLACK, (CELL_SIZE, 0), (CELL_SIZE, SCREEN_HEIGHT), 10)
    pygame.draw.line(screen, BLACK, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, SCREEN_HEIGHT), 10)

# Define a function to draw the symbols on the screen
def draw_symbols():
    # Loop through each cell of the board
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            # If the cell value is 1, draw an X
            if board[row][col] == 1:
                pygame.draw.line(screen, RED, (col * CELL_SIZE + 50, row * CELL_SIZE + CELL_SIZE - 50), (col * CELL_SIZE + CELL_SIZE - 50, row * CELL_SIZE + 50), 25)
                pygame.draw.line(screen, RED, (col * CELL_SIZE + 50, row * CELL_SIZE + 50), (col * CELL_SIZE + CELL_SIZE - 50, row * CELL_SIZE + CELL_SIZE - 50), 25)
            # If the cell value is -1, draw an O
            elif board[row][col] == -1:
                pygame.draw.circle(screen, BLUE, (col * CELL_SIZE + CELL_SIZE // 2 , row * CELL_SIZE + CELL_SIZE //2 ), 60 ,15)

# Define a function to mark a cell with a symbol
def mark_cell(row , col , player):
    # Mark the cell value with either 1 or -1 depending on the player
    board[row][col] = player

# Define a function to check if a cell is empty
def is_cell_empty(row , col):
    # Return True if the cell value is zero
    return board[row][col] == 0

# Define a function to check if the board is full
def is_board_full():
    # Return True if there are no zeros in the board array
    return not np.any(board == 0)

# Define a function to check for a win
def check_win(player):
    # Check for horizontal win
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    
    # Check for vertical win
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    
    # Check for diagonal win
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    # Return False if no win is found
    return False

# Define a function to restart the game
def restart():
    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw the lines on the screen
    draw_lines()

    # Reset the board array to zeros
    board = np.zeros((BOARD_ROWS, BOARD_COLS))

# Define the player variable (1 for X, -1 for O)
player = 1

# Fill the screen with white color
screen.fill(WHITE)

# Draw the lines on the screen
draw_lines()

# Define a variable to store the game over state
game_over = False

# Main loop of the game
while True:
    # Loop through the events in the game
    for event in pygame.event.get():
        # If the event is pygame.QUIT, exit the game
        if event.type == pygame.QUIT:
            sys.exit()
        # If the event is pygame.MOUSEBUTTONDOWN and the game is not over
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            # Get the x and y position of the mouse
            x = event.pos[0]
            y = event.pos[1]

            # Convert the x and y position to row and col indices
            row = y // CELL_SIZE
            col = x // CELL_SIZE

            # If the cell is empty, mark it with the player symbol
            if is_cell_empty(row, col):
                mark_cell(row, col, player)
                # Check for a win
                if check_win(player):
                    game_over = True
                # Switch the player turn
                player *= -1
    
    # Draw the symbols on the screen
    draw_symbols()

    # Update the display
    pygame.display.update()
