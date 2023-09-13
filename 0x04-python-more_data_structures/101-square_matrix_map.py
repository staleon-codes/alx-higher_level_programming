#!/usr/bin/python3
# Python program that:
# demonstrates how to compute the square value of all integers of a matrix

def square_matrix_map(matrix=[]):
    return list(map(lambda l: list(map(lambda n: n*n, l)), matrix))
