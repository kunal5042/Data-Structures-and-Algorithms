# Question: https://leetcode.com/problems/unique-paths/
# Medium

from typing import Optional, List

class Solution:
    # O(m*n) time and O(m*n) space
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

    # O(m*n) time and O(m*n) space
    # [Solved again, although doesn't seem like it]
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for _ in range(n)] for _ in range(m)]
        for col in range(n): paths[0][col] = 1
        for row in range(m): paths[row][0] = 1
        
        for row in range(1, m):
            for col in range(1, n):
                paths[row][col] = paths[row-1][col] + paths[row][col-1]
        
        return paths[~0][~0]
'''

# Kunal Wadhwa

'''