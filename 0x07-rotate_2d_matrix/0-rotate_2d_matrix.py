#!/usr/bin/python3
"""
0-rotate_2d_matrix.py

This script rotates a given n x n 2D matrix 90 degrees matrix
clockwise in-place.
The function 'rotate_2d_matrix' first transposes the
matrix (i.e., flips it over its diagonal),
and then reverses each row. The result is a 90-degree
clockwise rotation of the original matrix.

The function modifies the input matrix in-place.
You can print the matrix after
calling the function to see the rotated matrix.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): The input 2D matrix to be rotated.
                                        It's assumed to be a square
                                        matrix (n x n).

    Returns:
        None. The function modifies the input matrix in-place.
    """
    # Transpose the matrix here
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    # Reverse each row here
    for i in range(n):
        matrix[i] = matrix[i][::-1]
