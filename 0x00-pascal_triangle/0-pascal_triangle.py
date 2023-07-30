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
        if i == 0:
            row = [1]
        else:
            prev_row = triangle[i - 1]
            row = [1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)
        triangle.append(row)
    return triangle
