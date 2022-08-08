# Question: https://leetcode.com/problems/score-after-flipping-matrix/

from typing import Optional, List

class Solution:
    # O(HEIGHT * WIDTH) Time and O(1) Space
    def matrixScore(self, grid: List[List[int]]) -> int:
        HEIGHT, WIDTH = len(grid), len(grid[0])
        def flip_row(row_no):
            for idx in range(WIDTH):
                grid[row_no][idx] = 1 if grid[row_no][idx] != 1 else 0
                
                
        def flip_col(col_no):
            for idx in range(HEIGHT):
                grid[idx][col_no] = 1 if grid[idx][col_no] != 1 else 0                
        
        def get_score():
            score = 0
            for row in range(HEIGHT):
                for col in range(WIDTH):
                    if grid[row][col] == 1:
                        score += 2 ** (WIDTH-col-1)
                        
            return score
        
        def get_one_count(col_no):
            count = 0
            for row_no in range(HEIGHT):
                if grid[row_no][col_no] == 1: count += 1
            return count
        
        # make flips that will guarantee a higher number after the flip
        def make_good_flips():
            for row_no, row in enumerate(grid):
                if row[0] == 0: flip_row(row_no)
                    
            for col_no in range(WIDTH):
                one_count = get_one_count(col_no)
                if one_count <= HEIGHT // 2:
                    flip_col(col_no)
        
        make_good_flips()
        return get_score()
'''

# Kunal Wadhwa

'''