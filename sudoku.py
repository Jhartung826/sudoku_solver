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




def sudoku_solver(sudoku):
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

print(solved_p)

                    









