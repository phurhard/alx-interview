#!/usr/bin/python3
"""Making change LeetCode"""


def makeChange(coins, total):
    """Making change of total, given list of coins"""
    min_coins = -1
    solution = []
    coins_used = 1
    if total == 0 or total < 0:
        return 0
    for coin in coins:
        pass
