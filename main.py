import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()

# WINDOW SETUP
WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver using Backtracking")

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# FONTS
STAT_FONT = pygame.font.SysFont("comicsans", 35)

ran = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0], 
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0] 
]

def draw_grid(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                text = STAT_FONT.render(str(sudoku[i][j]), True, BLACK)
                textRect = text.get_rect()
                textRect.center = (j*WIDTH//9 + WIDTH//18, i*HEIGHT//9 + HEIGHT//18)
                window.blit(text, textRect)

def main():
    window.fill(WHITE)

    # draw the grid lines
    pygame.draw.line(window, BLACK, (0, WIDTH//3), (WIDTH, WIDTH//3), 2)
    pygame.draw.line(window, BLACK, (0, 2*WIDTH//3), (WIDTH, 2*WIDTH//3), 2)
    pygame.draw.line(window, BLACK, (WIDTH//3, 0), (WIDTH//3, HEIGHT), 2)
    pygame.draw.line(window, BLACK, (2*WIDTH//3, 0), (2*WIDTH//3, HEIGHT), 2)

    # draw the numbers
    draw_grid(ran)

running = True 
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    main()

    pygame.display.update()