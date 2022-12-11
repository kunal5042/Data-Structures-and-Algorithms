# Question: https://leetcode.com/problems/n-queens-ii/
# Hard
from typing import Optional, List

class Solution: 
    def totalNQueens(self, n: int) -> int:

        board = []

        # Build the chess board
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append('X')
            board.append(row)


        return self.count(board, 0)

    def count(self, board: List[List[str]], row: int) -> int:
        # If all rows have been traversed = all queens have been placed
        # We have found one way of placing N queens
        if row == len(board):
            return 1

        count = 0

        # For each row and col, check if it is safe to place the Queen
        for col in range(len(board)):
            # If safe, then place the Queens
            if self.isSafe(board, row, col):
                board[row][col] = 'Q'
                # Check if it is possible to place next queen
                count += self.count(board, row+1)

                # One you come out of the above recursion call
                # Backtrack the board for the next recursion call
                board[row][col] = 'X'


        return count

    # Checking in 3 directions, only above the current row as there won't be any Queens places below the current row
    def isSafe(self, board: List[List[str]], row: int, col: int) -> bool:

        # Up
        for i in range(1, row+1):
            if board[row-i][col] == 'Q':
                return False


        # Diagonal UP RIGHT
        for i in range(1, min(row, len(board)-col-1)+1):
            if board[row-i][col+i] == 'Q':
                return False

        # Diagonal UP LEFT
        for i in range(1, min(row, col)+1):
            if board[row-i][col-i] == 'Q':
                return False


        return True
'''

# Kunal Wadhwa

'''