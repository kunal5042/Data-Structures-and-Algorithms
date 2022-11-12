# Question: https://leetcode.com/problems/maximal-square/
# Medium

from typing import Optional, List

class Solution:
    # O(HEIGHT * WIDTH) Time and Space
    
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Using dynamic-programming
        # Storing side length
        
        HEIGHT, WIDTH = len(matrix), len(matrix[0])
        side_length = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
        
        largest_side_length = 0
        
        for row in range(HEIGHT):
            for col in range(WIDTH):
                if matrix[row][col] == '0': continue
                if any([row - 1 < 0, col - 1 < 0]):
                    side_length[row][col] = 1
                else:
                    side_length[row][col] = 1 + min(side_length[row-1][col]  ,
                                                    side_length[row][col-1]  ,
                                                    side_length[row-1][col-1] )
                    
                largest_side_length = max(side_length[row][col], largest_side_length)
                
        return largest_side_length ** 2
'''

# Kunal Wadhwa

'''