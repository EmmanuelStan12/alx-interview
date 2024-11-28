#!/usr/bin/python3
"""Changes confirmed within
"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """Fewest no of coins to get to total
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for j in range(coin, total + 1):
            dp[j] = min(dp[j], 1 + dp[j - coin])

    return dp[total] if dp[total] != float('inf') else -1
