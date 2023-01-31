# Question: https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/
# Medium

from typing import List

class Solution:
    # O(n) time and O(1) space
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        falling_time = 0
        
        for distance in left:
            falling_time = max(falling_time, distance)
            
        for distance in right:
            falling_time = max(falling_time, n - distance)
            
        return falling_time
            
        
                    
            


# January 31, 2023

'''

# Kunal Wadhwa

'''