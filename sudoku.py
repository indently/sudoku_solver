import itertools

# Grid (9x9)
matrix = 9


# Print out the solution
def print_solution(grid):
    global matrix
    print("Solution:")
    for x in range(matrix):
        for y in range(matrix):
            print(grid[x][y], end="  ")
        print()


# Helper function that solves for each box
def check_valid_move(grid, row, col, num):
    # Check if number can be placed on the x-axis
    for i in range(matrix):
        if grid[row][i] == num:
            return False

    # Check if number can be placed on the y-axis
    for i in range(matrix):
        if grid[i][col] == num:
            return False

    # Get current start row and column of a given block
    start_row_block = row - row % 3
    start_col_block = col - col % 3

    # Check if move is valid in the current square
    for x in range(3):
        for y in range(3):
            if grid[x + start_row_block][y + start_col_block] == num:
                return False
    return True


# Check for possibility to place number
# solve(hard_grid, row=4, col=5, num=5)


def solve_sudoku(grid, row, col):
    global matrix
    # Check if we've reached the end of the sudoku
    if row == matrix - 1 and col == matrix:
        return True

    # We've reached the end of the columns, move to the next row
    if col == matrix:
        row += 1
        col = 0

    # Check whether the square already has a value
    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)

    for num in range(1, matrix + 1):
        # If solving is possible, assign that solution to the square
        if check_valid_move(grid, row, col, num):
            # Assign correct number to square
            grid[row][col] = num

            if solve_sudoku(grid, row, col + 1):
                return True

        # If no valid moves, reset and try again
        grid[row][col] = 0

    # If we reach this, then there are no possible solutions...
    return False


# Let user insert their custom grid
def create_grid() -> []:
    user_grid = []
    for i in range(matrix):
        user_input = input(f"Enter row #{i + 1}: ")
        row = [int(number) for number in user_input]
        user_grid.append(row)

    # print("Final:", user_grid)
    # Flatten list, so we can count it
    grid_length = len(list(itertools.chain(*user_grid)))

    if grid_length == 81:
        return user_grid
    else:
        raise Exception(f'Invalid grid amount. Needed: 81, got: {grid_length}')
