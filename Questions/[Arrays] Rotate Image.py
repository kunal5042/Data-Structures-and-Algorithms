# Question: https://leetcode.com/problems/rotate-image/
# Medium
class Solution:
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
                
                
# Kunal Wadhwa