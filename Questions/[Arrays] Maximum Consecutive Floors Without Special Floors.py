# Question: https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/
# Medium
from typing import Optional, List

class Solution:
    # brute-force
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        floors = [False for _ in range(top-bottom+1)]
        
        for floor_id in special:
            floors[floor_id-bottom] = True
            
        result = 0
        current = 0
        for is_special in floors:
            if is_special == True:
                current = 0
                continue
                
            current += 1
            result = max(result, current)
            
        return result
    
    # O(n*log(n)) time and O(1) space: where n is the length of special array
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        result = 0
        special.append(top+1)
        special.sort()
        
        curr_bottom = bottom
        for curr_top in special:
            result = max(result, curr_top - curr_bottom)
            curr_bottom = curr_top + 1
        
        return result
            


# January 28, 2023

'''

# Kunal Wadhwa

'''