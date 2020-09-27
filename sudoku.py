import numpy as np
import random
import time
import math

puzzle = np.array([
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]])

testlist = [45,45,45,45,43]
# print(puzzle.shape[0])
# hi = 1
# for i in range(9):
#     hello = hi
#     hello +=1
# for i,j in zip([0,3,6], [0, 3, 6]):
#     # print(puzzle[i:i+3,j:j+3])
# for i in [0,3,6]:
#     for j in [0,3,6]:
#         # print(puzzle[i:i+3,j:j+3]) 
test = [puzzle[i:i+3,j:j+3] for i in [0,3,6] for j in [0,3,6]]
print(test[4])
# for i in range(9):
#     for j in range(9):
#         # print(j)
def quadrant_finder(mattrix, x, y):
    quads = [mattrix[i:i+3,j:j+3] for i in [0,3,6] for j in [0,3,6]]
    if x < 3:
        if y < 3:
            return quads[0]
        elif y < 6:
            return quads[1]
        else:
            return quads[2]
    elif x < 6:
        if y < 3:
            return quads[3]
        elif y < 6:
            return quads[4]
        else:
            return quads[5]
    else:
        if y < 3:
            return quads[6]
        elif y < 6:
            return quads[7]
        else:
            return quads[8]









def sudoku_solver(sudoku):
    # save the unsolved puzzle
    Solved = False
    unsolved = np.zeros([9,9])
    while Solved==False:
        for i in range(9):
            for j in range(9):
                if sudoku[i][j] == 0:
                    possible_nums = []
                    for num in range(1,10):
                        if (not num in unsolved[i]) and (not num in unsolved[:,j]) and (not num in sudoku[i]) and (not num in sudoku[:,j]) and (not num in quadrant_finder(sudoku, i, j)) and (not num in quadrant_finder(unsolved, i, j)):
                            possible_nums.append(num)
                    print(len(possible_nums))
                    if len(possible_nums) == 1:
                        unsolved[i][j] = possible_nums[0]
                else:
                    unsolved[i][j] = sudoku[i][j]
        
        threebythree = [sum(sum(unsolved[i:i+3,j:j+3])) for i in [0,3,6] for j in [0,3,6]]
        rows = [sum(unsolved[i]) for i in range(unsolved.shape[0])]
        cols = [sum(unsolved[:,j]) for j in range(unsolved.shape[1])]

        if len(set(threebythree)) == 1 and len(set(rows)) == 1 and len(set(cols)) == 1:
            solved = unsolved
            Solved = True
    return solved


solved_p = sudoku_solver(puzzle)

# print(puzzle[8][8])
# print(puzzle[:,8])
# print(puzzle[8])
print("it worked!!!!")
print(solved_p)

                    









