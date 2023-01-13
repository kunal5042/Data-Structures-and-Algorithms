# Question: https://leetcode.com/problems/maximum-matrix-sum
# Medium
from typing import Optional, List

class Solution:
    # O(n*m) time and O(1) space
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        negatives = 0
        zeroes = 0
        minimum = float('inf')
        _sum = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0: zeroes += 1
                if matrix[row][col] <  0: negatives += 1
                minimum = min(minimum, abs(matrix[row][col]))
                _sum += abs(matrix[row][col])
                
        if zeroes >= 1 or negatives % 2 == 0: return _sum
        return _sum - 2*minimum


# January 13, 2023

'''

# Kunal Wadhwa

'''