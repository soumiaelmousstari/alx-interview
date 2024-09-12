#!/usr/bin/python3
"""0x07. Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate
    it 90 degrees clockwise."""
    n = len(matrix)
    for rang_x in range(n):
        tmp = []
        for rang_y in range((n - 1), -1, -1):
            tmp.append(matrix[rang_y][rang_x])
        matrix.append(tmp)
    for i in range(n):
        matrix.pop(0)
