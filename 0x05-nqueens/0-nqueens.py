#!/usr/bin/env python3
"""Solving the nqueens problem in chess"""
import sys


def queens():
    """The queens function"""
    # the checks
    if len(sys.argv) > 2 or len(sys.argv) == 1:
        print('Usage: nqueens N')
        sys.exit(1)
    n = sys.argv[1]
    try:
        n = int(n)
    except Exception:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)
    # create a matrix/board
    matrix = [[0] * n for _ in range(n)]
    COLUMNS = set()
    POSDIA = set()
    NEGDIA = set()

    def backtrack(r):
        """The backtracking is sweet"""
        if r < n:
            for c in range(n):
                if c in COLUMNS or (r + c) in POSDIA or (r - c) in NEGDIA:
                    continue
                COLUMNS.add(c)
                POSDIA.add(r + c)
                NEGDIA.add(r - c)
                matrix[r][c] = 'Q'
                backtrack(r + 1)
                COLUMNS.remove(c)
                POSDIA.remove(r + c)
                NEGDIA.remove(r - c)
                matrix[r][c] = '0'
        if r == n:
            # print(matrix)
            ans = [[row, c] for row in range(n) for c in range(n)
                   if matrix[row][c] == 'Q']
            print(ans)
            return
    backtrack(0)


queens()
