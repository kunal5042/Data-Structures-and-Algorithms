# Question: https://leetcode.com/problems/spiral-matrix-ii/
# Medium
from typing import Optional, List

class Solution:
    # O(n*n) time and O(1) space
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        colstart, colend = 0, len(matrix[0])
        rowstart, rowend = 0, len(matrix)
        currow  , curcol = 0, len(matrix[0])-1
        toprow  , botrow = 0, len(matrix)-1
        leftcol , rightcol = 0, len(matrix[0])-1
        
        ele = 1
        
        while leftcol <= rightcol and toprow <= botrow:

            for col in range(colstart, colend):
                matrix[toprow][col] = ele
                ele += 1

            toprow += 1
            rowstart += 1
            
            for row in range(rowstart, rowend):
                matrix[row][rightcol] = ele
                ele += 1

            rightcol -= 1
            colend   -= 1
            rowend   -= 1
            
            for col in reversed(range(colstart, colend)):
                matrix[botrow][col] = ele
                ele += 1

            botrow   -= 1
            colstart += 1

            for row in reversed(range(rowstart, rowend)):
                matrix[row][leftcol] = ele
                ele += 1

            leftcol  += 1
            
        return matrix
            


# December 27, 2022

'''

# Kunal Wadhwa

'''