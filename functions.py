from puzzle import *

def printSudoku(sudoku):
    print("-------------------------")
    for i in range(LEN_ROWS):
        print("|", end=" ")
        

        for j in range(LEN_COLUMNS):
            print(sudoku[i][j], end=" ")
            if (j+1) % 3 == 0:
                print("|", end=" ")
        print()
        if (i+1) % 3 == 0:
            print("-------------------------")

def getBoxBits(numBox):
    match numBox:
        case 1:
            boxRange = [[0, 2], [0, 2]]
        case 2:
            boxRange = [[0, 2], [3, 5]]
        case 3:
            boxRange = [[0, 2], [6, 8]]
        case 4:
            boxRange = [[3, 5], [0, 2]]
        case 5:
            boxRange = [[3, 5], [3, 5]]
        case 6:
            boxRange = [[3, 5], [6, 8]]
        case 7:
            boxRange = [[6, 8], [0, 2]]
        case 8:
            boxRange = [[6, 8], [3, 5]]
        case 9:
            boxRange = [[6, 8], [6, 8]]
        case _:
            return

    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(boxRange[0][0], boxRange[0][1]+1):
        for j in range(boxRange[1][0], boxRange[1][1]+1):
            if sudoku[i][j] != 0:
                nums[sudoku[i][j] - 1] = 1

    return nums

def countZeros(sudoku):
    count = 0
    for i in range(LEN_ROWS):
        for j in range(LEN_COLUMNS):
            if sudoku[i][j] == 0:
                count += 1
    return count

def getBoxNumber(row, column):
    if row < 3:
        if column < 3:
            return 1
        elif column < 6:
            return 2
        else:
            return 3
    elif row < 6 and row > 2:
        if column < 3:
            return 4
        elif column < 6:
            return 5
        else:
            return 6
    else:
        if column < 3:
            return 7
        elif column < 6:
            return 8
        else:
            return 9

def checkPuzzle(row, column):

    if sudoku[row][column] != 0:
        return False

    bits = getBoxBits(getBoxNumber(row, column))

    # loop in a row
    for i in range(LEN_COLUMNS):
        if sudoku[row][i] != 0:
            bits[sudoku[row][i] - 1] = 1

    # loop in a column
    for j in range(LEN_ROWS):

        if bits[sudoku[j][column] - 1] == 1:
            continue

        if sudoku[j][column] != 0:
            bits[sudoku[j][column] - 1] = 1

    if bits.count(0) == 1:
        sudoku[row][column] = bits.index(0) + 1
        return True

    return False