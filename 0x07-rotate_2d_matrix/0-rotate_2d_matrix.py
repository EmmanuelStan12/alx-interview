#!/usr/bin/python3
"""Rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate 2d matrix
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    for row in matrix:
        row.reverse()
