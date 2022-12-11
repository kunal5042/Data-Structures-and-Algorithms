# Question: https://leetcode.com/problems/search-a-2d-matrix-ii/
# Medium
from typing import Optional, List

class Solution:
    # O(m + n) Time and O(1) Space
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n-1
        
        while 0 <= row < m and 0 <= col < n:
            if matrix[row][col] > target:
                col -= 1
                continue
                
            if matrix[row][col] < target:
                row += 1
                continue
                
            return True
        
        return False
'''

# Kunal Wadhwa

'''