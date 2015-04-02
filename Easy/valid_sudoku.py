#!usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wenzhiquan'


class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean

    def isValidSudoku(self, board):
        if not board:
            return False

        # row
        for i in range(len(board)):
            temp = []
            for j in board[i]:
                if j in temp:
                    return False
                elif j != '.':
                    temp.append(j)

        # column
        for i in range(len(board)):
            temp = []
            for j in range(len(board)):
                element = board[j][i]
                if element in temp:
                    return False
                elif element != '.':
                    temp.append(element)

        # block
        block = 9
        loop = 3
        for index in range(block):
            row = index % 3 * 3
            column = index // 3 * 3
            temp = []
            for i in range(loop):
                for j in range(loop):
                    element = board[row + i][column + j]
                    if element in temp:
                        return False
                    elif element != '.':
                        temp.append(element)
                        print(temp)

        return True

if __name__ == "__main__":
    so = Solution()
    # board = [
    #     [5, 3, '.', '.', 7, '.', '.', '.', '.'],
    #     [6, '.', '.', 1, 9, 5, '.', '.', '.'],
    #     ['.', 9, 8, '.', '.', '.', '.', 6, '.'],
    #     [8, '.', '.', '.', 6, '.', '.', '.', 3],
    #     [4, '.', '.', 8, '.', 3, '.', '.', 1],
    #     [7, '.', '.', '.', 2, '.', '.', '.', 6],
    #     ['.', 6, '.', '.', '.', '.', 2, 8, '.'],
    #     ['.', '.', '.', 4, 1, 9, '.', '.', 5],
    #     ['.', '.', '.', '.', 8, '.', '.', 7, 9]
    # ]
    board = [
        "....5..1.",
        ".4.3.....",
        ".....3..1",
        "8......2.",
        "..2.7....",
        ".15......",
        ".....2...",
        ".2.9.....",
        "..4......"
    ]
    print(so.isValidSudoku(board))
