#!/usr/bin/python3
"""Solving minimum operations
"""


def minOperations(n: int) -> int:
    """Calculate no of operations
    """
    if n == 1:
        return 0

    dp = [0] * (n + 1)
    for num in range(2, n + 1):
        dp[num] = num
        for factor in range(1, num // 2 + 1):
            if num % factor == 0:
                dp[num] = min(dp[num], dp[factor] + (num // factor))

    return dp[n]
