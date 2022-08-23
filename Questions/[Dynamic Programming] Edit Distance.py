# Question: https://leetcode.com/problems/edit-distance/
# Hard
from typing import Optional, List

class Solution:
    # O(len(word1) * len(word2)) Time and O(len(word1) * len(word2)) Space
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0: return len(word2)
        if len(word2) == 0: return len(word1)
        
        HEIGHT, WIDTH = len(word1), len(word2)
        changes = [[0 for _ in range(WIDTH+1)] for _ in range(HEIGHT+1)]
        
        for col in range(WIDTH+1):
            changes[0][col] = col
            
        for row in range(HEIGHT+1):
            changes[row][0] = row
            
        for row in range(1, HEIGHT+1):
            for col in range(1, WIDTH+1):
                if word1[row-1] == word2[col-1]:
                    changes[row][col] = changes[row-1][col-1]
                else:
                    changes[row][col] = min(changes[row][col-1], changes[row-1][col-1], changes[row-1][col]) + 1
                    
            
        return changes[~0][~0]
'''

# Kunal Wadhwa

'''