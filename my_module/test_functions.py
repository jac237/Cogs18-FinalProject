"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import *

##
##

test_cell_1 = [[0]*4]*4
test_cell_2 = [[0, 2, 8, 4], [16, 64, 4, 2], [8, 4, 32, 4], [2, 256, 8, 2]]
test_cell_3 = [[128, 2, 4, 2], [8, 4, 128, 4], [8, 512, 64, 64], [4, 16, 32, 4]]
test_cell_4 = [[4, 0, 0, 2], [0, 4, 0, 4], [2, 0, 0, 0], [0, 0, 32, 0]]

def same_board(board1, board2):
    for row1, row2 in zip(board1, board2):
        if row1 != row2:
            return False
    return True

def test_can_move_right():

    assert can_move_right(test_cell_1) == False
    assert can_move_right(test_cell_2) == False
    assert can_move_right(test_cell_3) == True
    assert can_move_right(test_cell_4) == True

def test_can_move_left():
    
    assert can_move_left(test_cell_1) == False
    assert can_move_left(test_cell_2) == True
    assert can_move_left(test_cell_3) == True
    assert can_move_left(test_cell_4) == True

def test_can_move_up():
    
    assert can_move_up(test_cell_1) == False
    assert can_move_up(test_cell_2) == True
    assert can_move_up(test_cell_3) == True
    assert can_move_up(test_cell_4) == True
    
def test_can_move_down():

    assert can_move_down(test_cell_1) == False
    assert can_move_down(test_cell_2) == False
    assert can_move_down(test_cell_3) == True
    assert can_move_down(test_cell_4) == True
    
test_row_1 = [0,2,0,2]
test_row_2 = [4,4,4,4]
test_row_3 = [2,4,0,0]
test_row_4 = [2,0,0,0]
test_row_5 = [0,0,2,0]
    
def test_shift_row_right():

    assert shift_row_right(test_row_1) == [0,0,2,2]
    assert shift_row_right(test_row_2) == [4,4,4,4]
    assert shift_row_right(test_row_3) == [0,0,2,4]
    assert shift_row_right(test_row_4) == [0,0,0,2]
    assert shift_row_right(test_row_5) == [0,0,0,2]
    
def test_shift_row_left():

    assert shift_row_left(test_row_1) == [2,2,0,0]
    assert shift_row_left(test_row_2) == [4,4,4,4]
    assert shift_row_left(test_row_3) == [2,4,0,0]
    assert shift_row_left(test_row_4) == [2,0,0,0]
    assert shift_row_left(test_row_5) == [2,0,0,0]
    
test_cell_1 = [[0]*4]*4
test_cell_2 = [[0, 8, 8, 0], [2, 2, 2, 2], [4, 4, 8, 8], [2, 256, 8, 2]]
test_cell_3 = [[128, 2, 0, 2], [4, 4, 128, 4], [8, 512, 64, 64], [4, 32, 32, 4]]
test_cell_4 = [[4, 0, 0, 2], [0, 4, 0, 4], [2, 0, 0, 0], [0, 0, 32, 0]]
    
def test_move_left():

    assert same_board(move_left(test_cell_1), [[0]*4]*4)
    assert same_board(move_left(test_cell_2), [[16,0,0,0], [4, 4, 0, 0], [8, 16, 0, 0], [2, 256, 8, 2]])
    assert same_board(move_left(test_cell_3), [[128, 4,0,0], [8, 128, 4,0], [8, 512, 128,0], [4, 64, 4, 0]])
    assert same_board(move_left(test_cell_4), [[4,2,0,0], [8,0,0,0], [2,0,0,0], [32,0,0,0]])
    
def test_move_right():

    assert same_board(move_right(test_cell_1), [[0]*4]*4)
    assert same_board(move_right(test_cell_2), [[0, 0, 0, 16], [0, 0, 4, 4], [0, 0, 8, 16], [2, 256, 8, 2]])
    assert same_board(move_right(test_cell_3), [[0, 0, 128, 4], [0, 8, 128, 4], [0, 8, 512, 128], [0, 4, 64, 4]])
    assert same_board(move_right(test_cell_4), [[0, 0, 4, 2], [0, 0, 0, 8], [0, 0, 0, 2], [0, 0, 0, 32]])

def test_move_up():

    assert same_board(move_up(test_cell_1), [[0]*4]*4)
    assert same_board(move_up(test_cell_2), [[2,8,8,2], [4,2,2,8], [2,4,16,2], [0,256,0,0]])
    assert same_board(move_up(test_cell_3), [[128,2,128,2], [4,4,64,4], [8,512,32,64], [4,32,0,4]])
    assert same_board(move_up(test_cell_4), [[4,4,32,2], [2,0,0,4],[0,0,0,0], [0,0,0,0]])

def test_move_down():

    assert same_board(move_down(test_cell_1), [[0]*4]*4)
    assert same_board(move_down(test_cell_2), [[0,8,0,0], [2,2,8,2], [4,4,2,8], [2,256,16,2]])
    assert same_board(move_down(test_cell_3), [[128,2,0,2], [4,4,128,4], [8,512,64,64], [4,32,32,4]])
    assert same_board(move_down(test_cell_4), [[0,0,0,0], [0,0,0,0], [4,0,0,2], [2,4,32,4]])

test_can_move_right()
test_can_move_left()
test_can_move_up()
test_can_move_down()
test_shift_row_right()
test_shift_row_left()
test_move_left()
test_move_right()
test_move_up()
test_move_down()