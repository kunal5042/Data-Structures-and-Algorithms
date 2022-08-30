# Question: https://leetcode.com/problems/rotate-image/
# Medium
# 
class Solution:
    # O(rows*cols) Time and O(1) Space
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for col in range(row+1, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            
        for row in matrix:
            left, right = 0, len(row)-1
            
            while left <= right:
                row[left], row[right] = row[right], row[left]
                left  += 1
                right -= 1

    def rotate(self, matrix):
        def transpose():
            _col = -1
            for row in range(len(matrix)):
                _col += 1
                for col in range(_col, len(matrix[row])):
                    matrix[row][col], matrix[col][row] = \
                    matrix[col][row], matrix[row][col]
                    
        def reverse_rows():
            for row in range(len(matrix)):
                left, right = 0, len(matrix[row])-1
                while left < right:
                    matrix[row][left] , matrix[row][right] = \
                    matrix[row][right], matrix[row][left]
                    left  += 1
                    right -= 1
                    
        transpose()
        reverse_rows()
                
                
# Kunal Wadhwa