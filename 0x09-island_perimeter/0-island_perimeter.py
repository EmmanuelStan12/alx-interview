#!/usr/bin/python3
"""Island perimeter
"""


def island_perimeter(grid):
    """Find the perimeter of an island
    """
    total = 0
    for i in range(1, len(grid) - 1):
        row = grid[i]
        for j in range(1, len(row) - 1):
            cell = row[j]
            if cell == 1:
                total += find_perimeter(i, j, grid)

    return total


def find_perimeter(row, col, grid):
    """Get the adjacent cells
    """
    left = grid[row][col - 1]
    right = grid[row][col + 1]
    top = grid[row - 1][col]
    bottom = grid[row + 1][col]
    p = 4 - left - right - top - bottom
    return p
