# Question: https://leetcode.com/problems/surrounded-regions/
# Medium
from typing import Optional, List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        HEIGHT, WIDTH = len(board), len(board[0])
        visited = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]
        
        def capture(row, col, chain):
            if visited[row][col] is True: return True
            
            if row == 0 or row == HEIGHT - 1: return False
            if col == 0 or col == WIDTH - 1 : return False
            
            visited[row][col] = True
            chain.append((row, col))
            can_capture = True
            
            for r, c in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 > row + r >= HEIGHT or 0 > col + c >= WIDTH:
                    continue
                    
                if board[row+r][col+c] == 'O':
                    if capture(row+r, col+c, chain) is False:
                        # not immediately returning false so that the entire chain can be marked
                        can_capture = False
                        
            return can_capture
        
        def update(chain):
            for row, col in chain: board[row][col] = 'X'
        
        for row in range(1, HEIGHT-1):
            for col in range(1, WIDTH-1):
                if board[row][col] == 'O' and visited[row][col] is False:
                    chain = []
                    if capture(row, col, chain) is True:
                        update(chain)
                    
                    
        
'''

# Kunal Wadhwa

'''