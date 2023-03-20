def is_valid_move(grid, row, col, number):
    for x in range(9):
        if grid[row][x] == number:
            return False
    
    for x in range(9):
        if grid[x][col] == number:
            return False
    
    conner_row = row - row % 3
    conner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[conner_row + x][conner_col + y] == number:
                return False
    return True


def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0
    
    if grid[row][col] > 0:
        return solve(grid, row, col + 1)
    
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

# fill the list of sudoku numbers where 0 represents an empty space
grid =[
    [0, 6, 8, 4, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 5, 0, 0, 0],
    [1, 4, 0, 0, 6, 0, 7, 0, 0],
    [4, 0, 0, 0, 3, 0, 0, 0, 0],
    [3, 0, 7, 0, 0, 0, 6, 0, 9],
    [0, 0, 0, 0, 7, 0, 0, 0, 3],
    [0, 0, 6, 0, 4, 0, 0, 3, 7],
    [0, 0, 0, 9, 0, 0, 0, 0, 0],
    [5, 0, 0, 0, 0, 3, 2, 1, 0]
]

if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end = " ")
        print()
else:
    print("No solution For this Sudoku")
