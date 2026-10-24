puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))


def is_valid(grid, row, col, num):
    # Check row
    if num in grid[row]:
        return False

    # Check column
    for r in range(9):
        if grid[r][col] == num:
            return False

    # Check 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if grid[r][c] == num:
                return False

    return True


def find_empty(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                return r, c
    return None

# Backtracking


def backtracking(grid, stats):
    empty = find_empty(grid)

    if empty is None:
        return True

    row, col = empty

    for num in range(1, 10):
        stats["attempts"] += 1

        if is_valid(grid, row, col, num):
            grid[row][col] = num

            if backtracking(grid, stats):
                return True

            grid[row][col] = 0

    stats["backtracks"] += 1
    return False

# Forward Checking


def get_domain(grid, row, col):
    return [
        num for num in range(1, 10)
        if is_valid(grid, row, col, num)
    ]


def forward_checking(grid, stats):
    empty = find_empty(grid)

    if empty is None:
        return True

    row, col = empty

    for num in get_domain(grid, row, col):
        stats["attempts"] += 1
        grid[row][col] = num

        valid = True

        # Check remaining empty cells
        for r in range(9):
            for c in range(9):
                if grid[r][c] == 0 and not get_domain(grid, r, c):
                    valid = False
                    break
            if not valid:
                break

        if valid and forward_checking(grid, stats):
            return True

        grid[row][col] = 0

    stats["backtracks"] += 1
    return False


# Run both methods
grid1 = [row.copy() for row in puzzle]
grid2 = [row.copy() for row in puzzle]

bt_stats = {"attempts": 0, "backtracks": 0}
fc_stats = {"attempts": 0, "backtracks": 0}

bt_solved = backtracking(grid1, bt_stats)
fc_solved = forward_checking(grid2, fc_stats)

print("Original Sudoku:")
print_grid(puzzle)

print("\nBacktracking Solution:")
if bt_solved:
    print_grid(grid1)
else:
    print("No solution exists.")

print("\nForward Checking Solution:")
if fc_solved:
    print_grid(grid2)
else:
    print("No solution exists.")

print("\nSearch Statistics:")
print("Backtracking Attempts:", bt_stats["attempts"])
print("Backtracking Backtracks:", bt_stats["backtracks"])
print("Forward Checking Attempts:", fc_stats["attempts"])
print("Forward Checking Backtracks:", fc_stats["backtracks"])
