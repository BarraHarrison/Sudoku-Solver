# Python Sudoku Solver

# Backtracking is an algorithm based on recursion
# The function explores all the possible choices from a given state
# It 'backtracks' to the previous state if there is no solution

def valid_move_function(grid, row, col, number):
    for x in range(9):
        if grid[row][x] == number:
            return False
        
    for x in range(9):
        if grid[x][col] == number:
            return False
        
    corner_row = row - row % 3
    corner_column = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_column + y] == number:
                return False
            
    return True

# Backtracking
def solve_function(grid, row, col):
    if col == 9:
        if row == 8:
            return True 
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve_function(grid, row, col + 1)
    
    for number in range(1, 10):
        if valid_move_function(grid, row, col, number):
            grid[row][col] = number
            if solve_function[grid, row, col + 1]:
                return True
            
        grid[row][col] = 0
    
    return False

grid = [
    [5, 4, 6, 8, 9, 2, 7, 1, 3],  
    [6, 7, 2, 1, 9, 5, 4, 8, 0],
    [1, 9, 8, 3, 4, 7, 6, 5, 2],
    [8, 5, 9, 7, 6, 1, 3, 2, 4],
    [4, 2, 0, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 6, 5],
    [9, 6, 1, 5, 3, 8, 2, 7, 0],
    [2, 8, 7, 4, 1, 9, 5, 3, 6],
    [3, 0, 5, 2, 8, 6, 1, 4, 9]
]

if solve_function(grid, 0, 0):
    for a in range(9):
        for b in range(9):
            print(grid[a][b], end=" ")
        print("---------")
else:
    print("There is no solution for this Sudoku puzzle.")