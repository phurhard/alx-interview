#!/usr/bin/python3
"""Minimum no of operations that can be carried out on a file"""


def minOperations(n):
    """min operatioon"""
    if n <= 1:
        return 0

    factors = []

    # Find prime factors of n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)

    if not factors:
        return 0

    return sum(factors)
