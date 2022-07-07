# Question: https://leetcode.com/problems/minimum-path-sum/

from typing import Optional, List

class Path:
    def __init__(self, min_path):
        self.min_path = min_path
    
class Solution:
    # runs faster than 99.96 % of all other python3 solutions
    def minPathSum(self, grid):
        (width, height)  = (len(grid[0]), len(grid))
        # using dynamic programming technique
        #
        # since we have only two choices at every point - go down or go right
        # to reach at a block[x][y] the minimum path will be minimum of path we took to reach block[x-1][y] and block[x][y-1]
        # where block[x-1][y] and block[x][y-1] store the minmum path to reach themselves
        #
        # hence we create another matrix in which we store the minimum path to reach every cell from the top left 
        # so minimum[x][y] = minimum path sum to reach grid[x][y]
        #
        # and we do this by following the relation minimum[x][y] = min(minimum[x-1][y], minimum[x][y-1]) + grid[x][y]
        # thereby, after we are done filling this minimum matrix
        # minimum[height][width] will have the minimum path sum we took to reach from top left to bottom right
        #
        # hence, we initialize this minimum matrix
        
        minimum = [[0 for _ in range(width)] for _ in range(height)]
        
        # base case for this dynamic programming relation
        minimum[0][0] = grid[0][0]

        # base case: because we can't apply the DP relation on the first row and the first column
        for col in range(1, width):
            minimum[0][col] = minimum[0][col-1] + grid[0][col]
            
        # base case: first column
        for row in range(1, height):
            minimum[row][0] = minimum[row-1][0] + grid[row][0]
        
        # applying DP relation on every remaining cell
        for x in range(1, height):
            for y in range(1, width):
                minimum[x][y] = min(minimum[x-1][y], minimum[x][y-1]) + grid[x][y]
        
        # result
        return minimum[height-1][width-1]
    
    # Recursive solution: very ineffecient
    def minPathSumIneffecient(self, grid):
        (width, height)  = (len(grid[0]), len(grid))
        
        # to store and update the minimum path in the recursive calls
        grid_paths = Path(float('inf'))
        
        # Logic: we can go either down, or right
        # so, explore all the paths starting from top left
        # that is: at every call or at every cell go both down and right
        # keep doing this until either we reach the last cell or we can't go any further because of out of bound
        #
        # while making calls keep track of the path sum
        # after reaching the last bottom right cell, update the minimum path sum accordingly 
        #
        def find_minimum_path_to_bottom_right(x, y, current_path, grid_paths):
            if x < 0 or x >= height or y < 0 or y >= width:
                return
            # keeping track of current path's sum
            current_path += grid[x][y]
            
            # checking if we reached the bottom right cell
            if x == height -1 and y == width - 1:
                grid_paths.min_path = min(grid_paths.min_path, current_path)
                return
            
            # exploring all options
            find_minimum_path_to_bottom_right(x, y+1, current_path, grid_paths)
            find_minimum_path_to_bottom_right(x+1, y, current_path, grid_paths)
            
        # starting with top left cell, exploring all the options
        find_minimum_path_to_bottom_right(0, 0, 0, grid_paths)
        
        # return minimum path
        return grid_paths.min_path
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''