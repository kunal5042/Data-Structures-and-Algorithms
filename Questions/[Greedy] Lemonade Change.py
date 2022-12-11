# Question: https://leetcode.com/problems/lemonade-change/
# Easy
from typing import Optional, List
from collections import defaultdict
class Solution:
    # O(n) time and O(1) space
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = defaultdict(int)
        
        for bill in bills:
            if bill == 20:
                if counts[5] == 0:return False

                if counts[10] > 0 and counts[5] > 0:
                    counts[10] -=1
                    counts[5] -= 1
                    continue
                    
                if counts[10] == 0:
                    if counts[5] < 3: return False
                    counts[5] -= 3
                
            if bill == 10:
                if counts[5] == 0:return False
                counts[5] -= 1
                
            counts[bill] += 1
            
        return True


# November 19, 2022

'''

# Kunal Wadhwa

'''