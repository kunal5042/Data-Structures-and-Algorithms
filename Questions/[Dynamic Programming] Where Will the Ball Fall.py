# Question: https://leetcode.com/problems/where-will-the-ball-fall/
# Medium
from typing import Optional, List

class Solution:
    # O(m*n) + O(n) Time
    def findBall(self, grid: List[List[int]]) -> List[int]:
        W, H = len(grid[0]), len(grid)
        dp = [[[] for _ in range(W)] for _ in range(H)]
        
        # one ball falls in one column each, initially
        for col in range(W):
            dp[0][col].append(col)

        for row in range(H):
            for col in range(0, W):
                # deadend with left wall
                if grid[row][col] == 1 and col == W-1:
                    dp[row][col].clear()
                    continue
                    
                # deadend because of a V formation
                if grid[row][col] == 1 and col + 1 < W and grid[row][col+1] == -1:
                    dp[row][col].clear()
                    continue

                # deadend with right wall
                if grid[row][col] == -1 and col == 0:
                    dp[row][col].clear()
                    continue
                    
                # deadend because of a V formation
                if grid[row][col] == -1 and col - 1 >= 0 and grid[row][col-1] == 1:
                    dp[row][col].clear()
                    continue

                # ball from row-1, col-1 falls in current cell if possible
                if row -1 >= 0 and col - 1 >= 0 and grid[row-1][col-1] == 1:
                    if len(dp[row-1][col-1]) != 0:
                        for cid in dp[row-1][col-1]:
                            dp[row][col].append(cid)

                # ball from row-1, col+1 falls in current cell if possible
                if row -1 >= 0 and col + 1 < W and grid[row-1][col+1] == -1:
                    if len(dp[row-1][col+1]) != 0:
                        for cid in dp[row-1][col+1]:
                            dp[row][col].append(cid)

        result = [-1 for _ in range(W)]
        for col in range(0, W):
            # if a ball reaches this column
            if len(dp[H-1][col]) != 0:
                
                # calculate where will it go from here
                offset = 1 if grid[H-1][col] == 1 else -1
                
                # update the result
                for cid in dp[H-1][col]:
                    if col + offset < 0 or col + offset >= W: continue 
                    result[cid] = col + offset

        return result 
'''

# Kunal Wadhwa

'''