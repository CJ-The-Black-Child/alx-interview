#!/bin/python3
def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int):m The number of rows in Pascal's triangle to generate

    Returns:
        list of lists: A lis of lists f integers representing Pascal's triangle up to n rows.
                        Returns an empty list if n <= 0.
    """
    listitem = []
    for i in range(n):
        temp_list = []
        for j in range(i+1):
            if j == 0 or j == i:
                temp_list.append(1)
            else:
                temp_list.append(listitem[i-1][j] + listitem[i-1][j-1])
        listitem.append(temp_list)
    return listitem