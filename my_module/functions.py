"""A collection of function for doing my project."""

# Setup - run this cell before doing the next part of the assignment
#   This cell imports some extra code, making it available for us to use later

import random
import string

from time import sleep
from IPython.display import clear_output

def can_move_right(cells):
    row_end = len(cells)
    col_end = len(cells[0])
    
    for row_i in range(0, row_end):
        
        for col_j in range(0, col_end - 1):
            
            curr_num = cells[row_i][col_j]
            right_num = cells[row_i][col_j + 1]
            
            if curr_num != 0 and right_num == 0:
                return True
            
            if curr_num == right_num != 0:
                return True
            
    return False

def can_move_left(cells):
    row_end = len(cells)
    col_end = len(cells[0])
    
    for row_i in range(0, row_end):
        
        for col_j in range(col_end - 1, 0, -1):
            
            curr_num = cells[row_i][col_j]
            left_num = cells[row_i][col_j - 1]
            
            if left_num == 0 and curr_num != 0:
                return True
            
            if left_num == curr_num != 0:
                return True
            
    return False

def can_move_up(cells):
    row_end = len(cells)
    col_end = len(cells[0])
            
    for col_j in range(0, col_end):
        
        for row_i in range(row_end - 1, 0, -1):
            
            curr_num = cells[row_i][col_j]
            top_num = cells[row_i - 1][col_j]
            
            if curr_num != 0 and top_num == 0:
                return True
            
            if curr_num == top_num != 0:
                return True
            
    return False

def can_move_down(cells):
    row_end = len(cells)
    col_end = len(cells[0])
            
    for col_j in range(0, col_end):
        
        for row_i in range(0, row_end - 1):
            
            curr_num = cells[row_i][col_j]
            bottom_num = cells[row_i + 1][col_j]
            
            if curr_num != 0 and bottom_num == 0:
                return True
            
            if curr_num == bottom_num != 0:
                return True
            
    return False

def shift_row_right(row):
    size = len(row)
    copy = list(filter(lambda x: (x != 0), row))
    copy = [0] * (size - len(copy)) + copy
    
    return copy

def shift_row_left(row):
    size = len(row)
    copy = list(filter(lambda x: (x != 0), row))
    copy = copy + [0] * (size - len(copy))
    
    return copy

def combine_row_left(row):
    row = row.copy()
    curr = 0
    end = len(row)
    
    while curr < end - 1:

        curr_num = row[curr]
        right_num = row[curr + 1]

        if curr_num == right_num != 0:
            row[curr] = curr_num + curr_num
            row[curr + 1] = 0
            curr += 1

        curr += 1
    
    return row

def combine_row_right(row):
    
    row = row.copy()
    curr = len(row) - 1
        
    while curr > 0:

        curr_num = row[curr]
        left_num = row[curr - 1]

        if left_num == curr_num != 0:
            row[curr] = curr_num + curr_num
            row[curr - 1] = 0
            curr -= 1

        curr -= 1
    
    return row

def move_right(cells):
    
    cells = cells.copy()
    row_end = len(cells)
    col_end = len(cells[0])
    
    for row_i in range(0, row_end):
        
        new_row = shift_row_right(cells[row_i])
        
        new_row = combine_row_right(new_row)
            
        cells[row_i] = shift_row_right(new_row)
    
    return cells

def move_left(cells):
    
    cells = cells.copy()
    row_end = len(cells)
    col_end = len(cells[0])
    
    for row_i in range(0, row_end):

        new_row = shift_row_left(cells[row_i])

        new_row = combine_row_left(new_row)

        cells[row_i] = shift_row_left(new_row)
    
    return cells

def move_up(cells):
    
    cells = cells.copy()
    row_end = len(cells)
    col_end = len(cells[0])
    
    for col_j in range(0, col_end):
        
        new_col = [cells[row_i][col_j] for row_i in range(0, row_end)]
        
        new_col = shift_row_left(new_col)
        
        new_col = combine_row_left(new_col)
        
        new_col = shift_row_left(new_col)
        
        for row_i, num in zip(range(0, row_end), new_col):
            
            cells[row_i][col_j] = num
            
    return cells

def move_down(cells):
    
    cells = cells.copy()
    row_end = len(cells)
    col_end = len(cells[0])
    
    for col_j in range(0, col_end):
        
        new_col = [cells[row_i][col_j] for row_i in range(0, row_end)]
        
        new_col = shift_row_right(new_col)
        
        new_col = combine_row_right(new_col)
        
        new_col = shift_row_right(new_col)
        
        for row_i, num in zip(range(0, row_end), new_col):
            
            cells[row_i][col_j] = num
            
    return cells