#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # rowC = set()
    # colC = set()
    perimeter = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2
                # rowC.add(r)
                # colC.add(c)
    # peri = len(rowC) + len(colC)
    return perimeter
