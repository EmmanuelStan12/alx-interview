#!/usr/bin/python3
"""Changes confirmed within
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Fewest no of coins to get to total
    """
    n = len(coins)
    dp = [[float('inf')] * (total + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        for j in range(total + 1):
            dp[i][j] = dp[i - 1][j]

            if j >= coins[i - 1]:
                dp[i][j] = min(dp[i][j], 1 + dp[i][j - coins[i - 1]])

    return dp[n][total] if dp[n][total] != float('inf') else -1
