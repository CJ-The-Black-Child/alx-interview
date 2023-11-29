#!/usr/bin/python3
"""
This module handles the Pascal's implementation
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int):m The number of rows in Pascal's triangle to generate

    Returns:
        list of lists: A list of lists f integers representing
                        Pascal's triangle up to n rows.
                        Returns an empty list if n <= 0.
    """
    res = []
    try:
        n = int(n)
    except ValueError:
        return res
    if n <= 0:
        return res
    for i in range(n):
        temp_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(res[i-1][j] + res[i-1][j-1])
        res.append(temp_list)
    return res
