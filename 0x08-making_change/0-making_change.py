#!/usr/bin/python3
"""Making change LeetCode"""


from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Making change of total, given list of coins"""
    if total < 0 or total == 0:
        return 0
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for a in range(1, total + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[total] if dp[total] != total + 1 else -1
