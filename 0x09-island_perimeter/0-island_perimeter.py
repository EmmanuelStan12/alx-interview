#!/usr/bin/python3
"""Island perimeter
"""


def island_perimeter(grid):
    """Find the perimeter of an island
    """
    if type(grid) != list:
        return 0
    total = 0
    for i in range(0, len(grid)):
        row = grid[i]
        for j in range(0, len(row)):
            cell = row[j]
            if cell == 0:
                continue
            total += find_perimeter(i, j, grid)

    return total


def find_perimeter(row, col, grid):
    """Get the adjacent cells
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[row])
    if row == 0 or (len(grid[row - 1]) > col and grid[row - 1][col] == 0):
        perimeter += 1
    if row == rows - 1 or (len(grid[row + 1]) > col and grid[row + 1][col] == 0):
        perimeter += 1
    if col == 0 or grid[row][col - 1] == 0:
        perimeter += 1
    if col == cols - 1 or (cols > col + 1 and grid[row][col + 1] == 0):
        perimeter += 1
    return perimeter
