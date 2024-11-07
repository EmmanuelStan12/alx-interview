#!/usr/bin/python3
"""N queens module
"""
import sys


def parse_input() -> int:
    """Retrieves and validates this program's input argument.
    """
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def solve_n_queens():
    """Solves the n queens problem
    """
    N = parse_input()

    def backtrack(row):
        """Backtracks the solutions
        """
        if row == N:
            board = [[r, col] for r, col in enumerate(q_pos)]
            solutions.append(board)
            return

        for col in range(N):
            diag = row - col
            anti_d = row + col
            if col not in cols and diag not in diagonals:
                if anti_d not in anti_diagonals:
                    q_pos[row] = col
                    cols.add(col)
                    diagonals.add(row - col)
                    anti_diagonals.add(row + col)

                    backtrack(row + 1)

                    cols.remove(col)
                    diagonals.remove(row - col)
                    anti_diagonals.remove(row + col)

    solutions = []
    cols = set()
    diagonals = set()
    anti_diagonals = set()
    q_pos = [-1] * N

    backtrack(0)
    return solutions


solutions = solve_n_queens()
for solution in solutions:
    print(solution)
