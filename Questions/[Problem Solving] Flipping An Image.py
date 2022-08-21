# Question: https://leetcode.com/problems/flipping-an-image/
# Easy
from typing import Optional, List

class Solution:
    # O(HEIGHT*WIDTH) and O(1) Space
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        HEIGHT, WIDTH = len(image), len(image[0])
        
        def reverse(row):
            left, right = 0, WIDTH-1
            
            while left < right:
                row[left], row[right] = row[right], row[left]
                left   += 1
                right  -= 1
                
        def invert(row):
            for idx in range(WIDTH):
                row[idx] = 1 if row[idx] == 0 else 0
        
        for row in image: reverse(row)
        for row in image: invert(row)
            
        return image
        
'''

# Kunal Wadhwa

'''