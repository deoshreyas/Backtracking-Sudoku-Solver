import pygame
from pygame.locals import *
from random import sample

# controls
# g - Generate Random Sudoku
# c - Check solution
# space - Solve automatically

pygame.init()
pygame.font.init()

# WINDOW SETUP
WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver using Backtracking")

# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FONTS
STAT_FONT = pygame.font.SysFont("comicsans", 35)

original_sudoku = [
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

variable_sudoku = [
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

def gen_sudoku():
    base  = 3
    side  = base*base
    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side
    # randomize rows, columns and numbers (of valid base pattern)
    def shuffle(s): return sample(s,len(s)) 
    rBase = range(base) 
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))
    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    squares = side*side
    empties = squares * 3//4
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0
    return board

def draw_grid(sudoku):
    for i in range(9):
        for j in range(9):
            if original_sudoku[i][j] != 0: # if a part of original grid, make it black
                text = STAT_FONT.render(str(sudoku[i][j]), True, BLACK)
                textRect = text.get_rect()
                textRect.center = (j*WIDTH//9 + WIDTH//18, i*HEIGHT//9 + HEIGHT//18)
                window.blit(text, textRect)
            elif sudoku[i][j] != 0: # if a part of new grid, make it red
                text = STAT_FONT.render(str(sudoku[i][j]), True, RED)
                textRect = text.get_rect()
                textRect.center = (j*WIDTH//9 + WIDTH//18, i*HEIGHT//9 + HEIGHT//18)
                window.blit(text, textRect)

def select(x, y):
    pygame.draw.rect(window, (0, 0, 0, 255), (x*WIDTH//9, y*HEIGHT//9, WIDTH//9, HEIGHT//9), 4)

def main():
    window.fill(WHITE)

    # draw the grid lines
    pygame.draw.line(window, BLACK, (0, WIDTH//3), (WIDTH, WIDTH//3), 2)
    pygame.draw.line(window, BLACK, (0, 2*WIDTH//3), (WIDTH, 2*WIDTH//3), 2)
    pygame.draw.line(window, BLACK, (WIDTH//3, 0), (WIDTH//3, HEIGHT), 2)
    pygame.draw.line(window, BLACK, (2*WIDTH//3, 0), (2*WIDTH//3, HEIGHT), 2)

    # draw the other lines 
    for i in range(9):
        pygame.draw.line(window, BLACK, (0, i*WIDTH//9), (WIDTH, i*WIDTH//9), 1)
    for i in range(9):
        pygame.draw.line(window, BLACK, (i*WIDTH//9, 0), (i*WIDTH//9, HEIGHT), 1)   

    # draw the numbers
    draw_grid(variable_sudoku)

running = True 
x, y = 0, 0
solving = False
num_keys = [K_1, K_2, K_3, K_4, K_5, K_6, K_7, K_8, K_9]
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            x, y = x//(WIDTH//9), y//(HEIGHT//9)
        if event.type == KEYDOWN:
            key = event.key
            if key in num_keys and not solving:
                if original_sudoku[y][x] == 0:
                    variable_sudoku[y][x] = num_keys.index(key) + 1
            elif key==K_g and not solving:
                original_sudoku = gen_sudoku()
                variable_sudoku = [row[:] for row in original_sudoku]
    
    main()
    select(x, y)

    pygame.display.update()