# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:24:49 2019
@author: raghu
source: https://medium.com/analytics-vidhya/sudoku-puzzle-solver-how-to-build-your-very-first-python-project-b2f4c3e2160e

modified by Sander van Oostveen
Date modefied: Jun 11 2020
"""
#uncomment the code below to initiate a puzzle board
#instead of loading it from a file
# =============================================================================
# board = [
#     [7, 8, 0, 4, 0, 0, 1, 2, 0],
#     [6, 0, 0, 0, 7, 5, 0, 0, 9],
#     [0, 0, 0, 6, 0, 1, 0, 7, 8],
#     [0, 0, 7, 0, 4, 0, 2, 6, 0],
#     [0, 0, 1, 0, 5, 0, 9, 3, 0],
#     [9, 0, 4, 0, 6, 0, 0, 0, 5],
#     [0, 7, 0, 3, 0, 0, 0, 1, 2],
#     [1, 2, 0, 0, 0, 7, 4, 0, 0],
#     [0, 4, 9, 2, 0, 6, 0, 0, 7]
# ]

board = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]

board2 = [
    [0,2,0,0,0,0,0,0,0],
    [0,0,0,6,0,0,0,0,3],
    [0,7,4,0,8,0,0,0,0],
    [0,0,0,0,0,3,0,0,2],
    [0,8,0,0,4,0,0,1,0],
    [6,0,0,5,0,0,0,0,0],
    [0,0,0,0,1,0,7,8,0],
    [5,0,0,0,0,9,0,0,0],
    [0,0,0,0,0,0,0,4,0]
]

board3 = [ [ 3, 0, 6, 5, 0, 8, 4, 0, 0 ],
           [ 5, 2, 0, 0, 0, 0, 0, 0, 0 ],
                   [ 0, 8, 7, 0, 0, 0, 0, 3, 1 ],
                   [ 0, 0, 3, 0, 1, 0, 0, 8, 0 ],
                   [ 9, 0, 0, 8, 6, 3, 0, 0, 5 ],
                   [ 0, 5, 0, 0, 9, 0, 6, 0, 0 ],
                   [ 1, 3, 0, 0, 0, 0, 2, 5, 0 ],
                   [ 0, 0, 0, 0, 0, 0, 0, 7, 4 ],
                   [ 0, 0, 5, 2, 0, 6, 3, 0, 0 ] ]
# =============================================================================# loading the puzzle from a file

# def findEmpty(board):
#     """
#     A method to find the next empty cell of the puzzle.
#     Iterates from left to right and top to bottom
#
#     Arguments:
#     board - a list of nine sub lists with 9 numbers in each sub list
#
#     Output:
#     A tuple (i, j) which is index of row, column
#     """
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] == 0:
#                 return (i, j) #row, column
#     return None

def valid(board, num, pos):
    """
    A method to find if a number num is valid or not

    Arguments:
    board - a list of nine sub lists with 9 numbers in each sub list
    num - a number between 1 to 9 both inclusive
    pos - a tuple (i, j) representing row, column

    Output:
    True if the number is valid in position pos of puzzle else False.
    """
    row = pos[0]
    column = pos[1]
    #checking rows
    for i in range(len(board[0])):
        if board[row][i] == num and column != i:
            return False
    #checking columns
    for i in range(len(board)):
        if board[i][column] == num and row != i:
            return False

    #checking box
    startRowBox = row//3
    startColumnBox= column//3
    for i in range(startRowBox*3, (startRowBox*3)+3):
        for j in range(startColumnBox*3, (startColumnBox*3)+3):
            if board[i][j] == num and row != i and column != j:
                return False
    return True


def solve(board, ind):
    """
    A method to solve the sudoku puzzle using the other functions defined.
    We use a simple recursion and backtracking method.

    Arguments:
    board - a list of nine sub lists with 9 numbers in each sub list

    Output:
    Returns True once the puzzle is successfully solved else False
    """
    # find = findEmpty(board)

    if ind is 81:
        return True
    row = int(ind / 9)
    col = int(ind % 9)

    for i in range(1,10):

        if valid(board, i, [row, col]):
            board[row][col] = i

            if solve(board, ind + 1):
                return True

            board[row][col] = 0
    return False


solve(board, 0)           #solving the puzzle
solve(board2, 0)
solve(board3, 0)
