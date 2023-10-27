#!/usr/bin/python3
"""
Pascal triangle
"""


def pascal_triangle(n):
    """Outputs the pascal traingle of n

    Keyword arguments:
    n -- the positive integer to get the pascal traingle of
    Return: A pascal triangle size of n
    """
    triangle = []
    if n <= 0:
        return []
    for i in range(n):
        row = [1]
        if i != 0:
            prev_row = triangle[i - 1]
            row.extend(prev_row[j - 1] + prev_row[j] for j in range(1, i))
            row.append(1)
        triangle.append(row)
    return triangle
