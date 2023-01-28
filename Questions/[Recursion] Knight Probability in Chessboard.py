# Question: https://leetcode.com/problems/knight-probability-in-chessboard/
# Medium
from typing import Optional, List

from functools import cache
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def travels(xcurr, ycurr, k):
            if xcurr < 0 or xcurr >= n or ycurr < 0 or ycurr >= n: 
                # We're already outside the grid, so probability of staying inside is 0
                return 0
            elif k == 0:
                # We're inside the grid and have no more moves to make
                return 1
            else:
                # Otherwise, we make one of 8 possible moves and find the probability of staying inside after 
                # k - 1 more moves. Because each move is equally likely, we average all of these probabilities.
                return (travels(xcurr + 2, ycurr + 1, k - 1) + 
                        travels(xcurr + 1, ycurr + 2, k - 1) + 
                        travels(xcurr - 1, ycurr + 2, k - 1) + 
                        travels(xcurr - 2, ycurr + 1, k - 1) + 
                        travels(xcurr - 2, ycurr - 1, k - 1) + 
                        travels(xcurr - 1, ycurr - 2, k - 1) + 
                        travels(xcurr + 1, ycurr - 2, k - 1) +   
                        travels(xcurr + 2, ycurr - 1, k - 1)) / 8

        return travels(row, column, k)     


# January 28, 2023

'''

# Kunal Wadhwa

'''