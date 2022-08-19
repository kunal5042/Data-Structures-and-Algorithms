# Question: https://leetcode.com/problems/set-matrix-zeroes/
# Medium
from typing import List, Optional
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row, first_col = False, False

        def find_zeroes(matrix):
            nonlocal first_row
            nonlocal first_col
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    if matrix[row][col] == 0:
                        if row == 0:
                            first_row = True
                        if col == 0:
                            first_col = True

                        matrix[row][0] = 0
                        matrix[0][col] = 0
                    
                    
        def columns_zero(matrix, col):
            for row in range(len(matrix)):
                matrix[row][col] = 0

        def rows_zero(matrix, row):
            for col in range(len(matrix[row])):
                matrix[row][col] = 0


        def set_zeroes(matrix):
            for row in matrix:
                print(row)
            
            for row in range(1, len(matrix)):
                if matrix[row][0] == 0:
                    rows_zero(matrix, row)
                    
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0:
                    columns_zero(matrix, col)
                    
            if first_row is True:
                rows_zero(matrix, 0)
                
            if first_col is True:
                columns_zero(matrix, 0)
                
        find_zeroes(matrix)
        set_zeroes(matrix)
        return
    
# Kunal Wadhwa
            