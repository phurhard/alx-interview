#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """Island Perimeter calculation"""

    row_count = set()
    coloum_count = set()
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                row_count.add(r)
                coloum_count.add(c)
    row = len(row_count) + len(coloum_count)
    return 2 * row
