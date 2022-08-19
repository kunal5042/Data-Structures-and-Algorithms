# Question: https://leetcode.com/problems/convert-1d-array-into-2d-array/
# Easy
from typing import Optional, List

class Solution:
    def construct2DArray(self, original, m, n):
        rows, cols = m, n
        
        if rows * cols != len(original): return list()
        
        result = [[None for _ in range(cols)] for _ in range(rows)]
        og_idx = 0
        
        for row in range(rows):
            for col in range(cols):
                result[row][col] = original[og_idx]
                og_idx += 1
                
        return result
            
            
        

# Kunal Wadhwa
