# Question: https://leetcode.com/problems/valid-sudoku
# Medium
from typing import Optional, List
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_map = defaultdict(list)
        for x in range(9):
            for y in range(9):
                char = board[x][y]
                if char != '.': 
                    if char in board_map:
                        for pos in board_map[char]:
                            if (pos[0]== x) or (pos[1] == y) or (pos[0]//3 == x//3 and pos[1]//3 == y//3):
                                return False
                    board_map[char].append((x,y))
   
        return True
'''

# Kunal Wadhwa

'''