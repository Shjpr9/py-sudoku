from functions import *
from puzzle import *

SOLVABLE = countZeros(sudoku)
flag = 1
while SOLVABLE != 0:
    t = SOLVABLE
    for i in range(LEN_ROWS):
        for j in range(LEN_COLUMNS):
            if(checkPuzzle(i, j)):
                SOLVABLE -= 1
    if t == SOLVABLE:
        flag = 0
        print("Puzzle is unsolvable")
        break
    
if flag == 1:
    print("Puzzle is solved")
    printSudoku(sudoku)