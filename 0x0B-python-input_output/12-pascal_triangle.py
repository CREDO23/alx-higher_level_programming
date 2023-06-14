#!/usr/bin/python3
'''This module contains the pascal triangle implementation'''


def pascal_triangle(n):
    '''This function implements the pascal triangulation'''

    arr = []

    if n <= 0:
        return []

    arr.append([1])

    for i in range(1, n):
        row = []
        row.append(1)
        for j in range(2, i+1):
            if (i <= 2):
                row.append(j)
            else:
                row.append(arr[i-1][j-1] + arr[i-1][j-2])
        row.append(1)
        arr.append(row)

    return arr
