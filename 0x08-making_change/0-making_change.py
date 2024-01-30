#!/usr/bin/python3
"""
This module contains a function that calculates the fewest number of coins
needed to meet a given amount total using a dynamic programming approach.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
