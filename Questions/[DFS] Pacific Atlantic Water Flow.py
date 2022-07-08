# Question: https://leetcode.com/problems/pacific-atlantic-water-flow/

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