#!/usr/bin/python3
"""Minimum Ops coding challenge"""


def minOperations(n):
    """
    Computes the fewest number of operations needed to result
    in exactly n H characters.
    """
    if not isinstance(n, int) or n <= 0:
        return 0

    ops_count = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            ops_count += factor
            n /= factor
        factor += 1

    return ops_count
