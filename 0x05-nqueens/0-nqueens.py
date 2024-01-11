#!/usr/bin/env python3
"""Solving the nqueens problem in chess"""
import sys


def queens():
    """The function"""
    try:
        if len(sys.argv) > 2:
            print('Usage: nqueens N\n')
            sys.exit(1)
        n = sys.argv[1]
        try:
            n = int(n)
        except Exception:
            print('N must be a number\n')
            sys.exit(1)
        if n < 4:
            print('N must be at least 4\n')
            sys.exit(1)
        else:
            print('Got here')
    except Exception as e:
        print(f'Exception got here as {e}')
        sys.exit(0)

# queens()
def Queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from Queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a

for solution in Queens(6, 0, [], [], []):
    print(solution)

