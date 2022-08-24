# Question: https://leetcode.com/problems/game-of-life/
# Medium
from typing import Optional, List

class Solution:
    # O(HEIGHT * WIDTH) Time and O(HEIGHT * WIDTH) Space
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        HEIGHT, WIDTH = len(board), len(board[0])
        state = [x.copy() for x in board]
        
        def get_live_neighbors(row, col) -> int:
            """Return the count of alive neighbors"""
            offset = [(0,-1),  (0,1), (-1,0), (1,0), (-1,-1), 
                      (1,1) , (-1,1), (1,-1)]
            live_count = 0
            for r, c in offset:
                nrow, ncol = row + r, col + c
                
                if nrow < 0 or nrow >= HEIGHT: continue
                if ncol < 0 or ncol >= WIDTH : continue
                    
                if state[nrow][ncol] == 1:
                    live_count += 1
                    
            return live_count
        
        for row in range(HEIGHT):
            for col in range(WIDTH):
                live_count = get_live_neighbors(row, col)
                
                # updates according to the rules
                if live_count < 2:
                    board[row][col] = 0
                    
                elif live_count == 2:
                    continue
                    
                elif live_count == 3:
                    if state[row][col] == 0:
                        board[row][col] = 1
                        
                elif live_count > 3:
                    board[row][col] = 0
        
'''

# Kunal Wadhwa

'''