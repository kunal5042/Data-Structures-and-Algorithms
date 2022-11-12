# Question: https://leetcode.com/problems/unique-paths/
# Medium

from typing import Optional, List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[0 for _ in range(n)] for _ in range(m)]
        
        # base case
        for col in range(n): ways[0][col] = 1
        for row in range(m): ways[row][0] = 1
            
        # classic dynamic programming
        for row in range(1, m):
            for col in range(1, n):
                ways[row][col] = ways[row-1][col] + ways[row][col-1]
                
        return ways[~0][~0]
'''

# Kunal Wadhwa

'''