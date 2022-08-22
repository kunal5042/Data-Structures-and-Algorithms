# Question: https://leetcode.com/problems/rotating-the-box/
# Medium
from typing import Optional, List

class Solution:
    # O(HEIGHT * (WIDTH^2)) Time and O(1) Space
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        HEIGHT, WIDTH = len(box), len(box[0])
        
        for row in range(HEIGHT):
            for col in reversed(range(WIDTH)):
                if box[row][col] == '#':
                    idx = col + 1
                    
                    while idx < WIDTH and box[row][idx] == '.':
                        idx += 1
                    
                    idx -= 1
                    box[row][col] = '.'
                    box[row][idx] = '#'
                    
        
        return zip(*box[::-1])
'''

# Kunal Wadhwa

'''