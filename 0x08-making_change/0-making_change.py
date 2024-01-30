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
    dp = [0] + [float('inf')] * total
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x%coin] = min(dp[x%coin], dp[(x - coin)%coin] + 1)
    return dp[total%coin] if dp[total%coin] != float('inf') else -1
