#!/usr/bin/python3
"""
Write a function that computes the square value of all integers of a matrix.
"""

def square_matrix_simple(matrix=[]):
    newMatrix = []
    for i in matrix:
        temp = []
        for j in i:
            temp.append(j*j)
        newMatrix.append(temp)
    return newMatrix
