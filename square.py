#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_correct_number(n):
    #Check if n is not divisible by 2 and n is greater than 0
    return (((n%2) != 0) and (n > 0))


def create_empty_square(n):
    #Returns list of nested lists with zeros as place holder
    square = []
    
    for row in range(n):
        square.append([])
        for column in range(n):
            square[row].append(0)
    return square


def build_magic_square(n, square):
    magic_square = square

    # Set the starting position for 1
    row, column = n//2, n-1

    for num in range(1, n**2+1):

        # Place number in current position 
        magic_square[row][column] = num

        # Find the next position by moving diagonally up and right
        row, column = (row-1)%n, (column+1)%n

        # If the next position is already filled, move down instead
        if magic_square[row][column]:
            row, column = (row+1)%n, (column-2)%n

    return magic_square


def print_magic_square(square):
    #Prints out the magic square in a readable format
    output = ""
    for row in square:
        for col in row:
            print(str(col), end=" ")
        print()


def check_magic_square(magic_square):
    n = len(magic_square)
    diagonal_right = diagonal_left = 0
    sum_rows = sum(magic_square[0]) #Sum first row
    
    #Check rows
    for row in magic_square:
        if sum_rows != sum(row):
            print("Incorrect!")
            return False

    #Check diagonals
    for i in range(n):
        diagonal_right += magic_square[i][i]
        diagonal_left += magic_square[i][n-i-1] 
    
    if (sum_rows != diagonal_right) and (sum_rows != diagonal_left):
        print("Incorrect!")
        return False

    print("Correct!")
    return True


def get_input():
    return int(input("Enter an odd integer: "))


def show_error():
    print("Please make sure you entered a positive odd integer ^_^")


def main():
    n = 0
    done = False
    while not done:
        n = get_input()
        
        if (is_correct_number(n)):
            square = create_empty_square(n)
            magic_square = build_magic_square(n, square)
            print_magic_square(magic_square)
            check_magic_square(square)
            done = True
        else:
            if (n == 0000): #Easter egg exit code :P
                print("Bye :D")
                break
            show_error()

    return 1

if __name__ == "__main__":
    main()
