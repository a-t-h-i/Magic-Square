#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_correct_number(n):
    #Check if n is not divisible by 2 and n is greater than 0
    return (((n%2) != 0) and (n > 0))

def create_empty_square(n):
    square = []
    
    for row in range(n):
        square.append([])
        for column in range(n):
            square[row].append(0)
    return square

def build_magic_square(n, square):
    # Initialize the magic square with zeros
    magic_square = [[0 for column in range(n)] for row in range(n)]
    # Set the starting position for 1
    row, column = n//2, n-1
    # Loop through all numbers from 1 to n^2
    for num in range(1, n**2+1):
        # Place the current number in the current position
        magic_square[row][column] = num
        # Find the next position by moving diagonally up and right
        row, column = (row-1)%n, (column+1)%n
        # If the next position is already filled, move down instead
        if magic_square[row][column]:
            row, column = (row+1)%n, (column-2)%n
    return magic_square

def verify_magic_square(square):
    return false
