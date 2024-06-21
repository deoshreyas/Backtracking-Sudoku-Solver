import pygame
from pygame.locals import *
from random import sample

# controls
# <g> - Generate Random Sudoku
# <c> - Check solution
# <SPACE> - Solve automatically

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

# For Backtracking 
def get_empty(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]== 0):
                l[0]= row
                l[1]= col
                return True
    return False

def used_in_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

def used_in_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True
    return False

def is_safe(arr, row, col, num):
    return (not used_in_row(arr, row, num) and
           (not used_in_col(arr, col, num) and
           (not used_in_box(arr, row - row % 3, 
                           col - col % 3, num))))

def solve_sudoku(arr):   
    l =[0, 0]   
    if(not get_empty(arr, l)):
        return True
    row = l[0]
    col = l[1]
    for num in range(1, 10):
        if(is_safe(arr, row, col, num)):
            arr[row][col]= num
            if(solve_sudoku(arr)):
                return True
            arr[row][col] = 0       
    return False

# Generates random sudoku (with multiple solutions possible)
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

# Draws the lines to make everything look pretty
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

# Select the square where player has clicked
def select(x, y):
    pygame.draw.rect(window, (0, 0, 0, 255), (x*WIDTH//9, y*HEIGHT//9, WIDTH//9, HEIGHT//9), 4)

# Main functions
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

original_sudoku = gen_sudoku()
solved_sudoku = [row[:] for row in original_sudoku]
solve_sudoku(solved_sudoku)
variable_sudoku = [row[:] for row in original_sudoku]

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
                solved_sudoku = [row[:] for row in original_sudoku]
                solve_sudoku(solved_sudoku)
                variable_sudoku = [row[:] for row in original_sudoku]
            elif key==K_c and not solving:
                for i in range(9):
                    for j in range(9):
                        if variable_sudoku[i][j] != solved_sudoku[i][j]:
                            variable_sudoku[i][j] = 0
                        else:
                            original_sudoku[i][j] = variable_sudoku[i][j]
            elif key==K_SPACE and not solving:
                solving = True
                solve_sudoku(variable_sudoku)
                solving = False
    
    main()
    select(x, y)

    pygame.display.update()