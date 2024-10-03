#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle up to the nth row.
    """
    if n == 0:
        return []

    result = [[1]]

    for i in range(1, n):
        prev_row = result[-1]
        cur_row = [1]

        for j in range(1, len(prev_row)):
            cur_row.append(prev_row[j - 1] + prev_row[j])

        cur_row.append(1)
        result.append(cur_row)

    return result
