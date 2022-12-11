# Question: https://leetcode.com/problems/pacific-atlantic-water-flow/
# Medium
# atlantic.intersection(pacific): where atlantic and pacific is a set of coordinates from which water can flow to their respective oceans
from typing import Optional, List

'''EFFECIENT'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS        = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def dfs(row, col, prev_height, visit):
            if (row, col) in visit                        or \
                row <0                  or col<0            or\
                row == ROWS             or col == COLS      or \
                heights[row][col] < prev_height:
                return
            
            visit.add((row, col))
            dfs(row+1, col, heights[row][col], visit)
            dfs(row-1, col, heights[row][col], visit)
            dfs(row, col+1, heights[row][col], visit)
            dfs(row, col-1, heights[row][col], visit)
        
        for col in range(COLS):
            dfs(0       , col, heights[0][col]      , pacific)
            dfs(ROWS-1  , col, heights[ROWS-1][col] , atlantic)
            
        for row in range(ROWS):
            dfs(row, 0      , heights[row][0]        , pacific)
            dfs(row, COLS-1 , heights[row][COLS-1]   , atlantic)
            
        return atlantic.intersection(pacific)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        HEIGHT, WIDTH = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def depth_first_search(row, col, ocean):
            if (row, col) in ocean:
                return
            
            ocean.add((row, col))
            
            for r, c in [(1,0), (0,1), (-1,0), (0,-1)]:
                if 0 <= row+r < HEIGHT and 0 <= col+c < WIDTH:
                    if heights[row][col] <= heights[row+r][col+c]:
                        depth_first_search(row+r, col+c, ocean)
        
        for col in range(WIDTH):
            depth_first_search(0, col, pacific)
            depth_first_search(HEIGHT-1, col, atlantic)
                
        for row in range(HEIGHT):
            depth_first_search(row, 0, pacific)
            depth_first_search(row, WIDTH-1, atlantic)
                
        return pacific.intersection(atlantic)
        
 
'''BRUTE-FORCE'''
class olution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        result    = list()

        def valid(row, col):
            atlantic = False
            pacific  = False
            visited  = dict()
            
            def dfs(row, col):
                nonlocal atlantic, pacific
                
                if (row, col) in visited: return
                visited[(row, col)] = True
                
                if row + 1 < len(heights):
                    if heights[row][col] >= heights[row+1][col]:
                        dfs(row+1, col)
                else:
                    atlantic = True
                        
                if row - 1 >= 0:
                    if heights[row][col] >= heights[row-1][col]:
                        dfs(row-1, col)
                else:
                    pacific = True
                
                if col + 1 < len(heights[row]):
                    if heights[row][col] >= heights[row][col+1]:
                        dfs(row, col+1)
                else:
                    atlantic = True
                    
                if col - 1 >= 0:
                    if heights[row][col] >= heights[row][col-1]:
                        dfs(row, col-1)
                else:
                    pacific = True
                    
            dfs(row, col)
            if atlantic is True and pacific is True:
                return True
            return False
        
        
        for row in range(len(heights)):
            for col in range(len(heights[row])):
                if valid(row,col):
                    result.append((row, col))
                    
        return result
'''

# Kunal Wadhwa


'''