# Question: https://leetcode.com/problems/zigzag-conversion/
# Medium
# Good Question
from typing import Optional, List

class Solution:
    # Optimized
    # O(n) Time and O(n) Space
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1: return s
        
        zigzag = [[] for _ in range(num_rows)]
        
        row = 0
        forward = True
        for idx in range(len(s)):
            zigzag[row].append(s[idx])
            
            row = row + 1 if forward is True else row - 1
                
            if row == num_rows:
                forward = False
                row -= 2
                continue
                
            if row == -1:
                forward = True
                row = 1
                
        result = ''
        for row in zigzag: result += ''.join(row)
        return result
                
            
    
    # Brute Force
    # O(num_rows * len(s)) Time and Space
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1: return s
        
        grid = [['' for _ in range(len(s))] for _ in range(num_rows)]
        
        idx = 0
        row, col = 0, 0
        diag = False
        
        while idx < len(s):
            if diag is False:
                grid[row][col] = s[idx]
                idx += 1
                
                # can't proceed down
                if row + 1 == num_rows:
                    diag = True
                    row -= 1
                    col += 1
                else:
                    row += 1
                    
            else:
                grid[row][col] = s[idx]
                idx += 1
                
                # can't proceed diagonally
                if row - 1 < 0:
                    diag = False
                    row += 1
                    
                else:
                    row -= 1
                    col += 1
                    
        # generate result
        result = ''
        for row in grid: result += ''.join(row)
        return result

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        result = []
        gap = 2 * (numRows - 1)
        
        for row in range(numRows):
            idx = row
            
            while idx < len(s):
                result.append(s[idx])
                
                if row != 0 and row != numRows-1:
                    second = idx + (gap - (2 * row))
                    
                    if second < len(s):
                        result.append(s[second])
                        
                idx += gap
                
        return ''.join(result)
'''

# Kunal Wadhwa

'''