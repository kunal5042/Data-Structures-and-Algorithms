# Question: https://leetcode.com/problems/airplane-seat-assignment-probability/
# Medium
from typing import Optional, List

class Solution:
    # O(1) time and O(1) space
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n > 2: return 1 / 2
        return 1 / n
    
    # dynamic-programming
    # O(n) time and O(1) space
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1: return 1
        
        previous = 1.0/n                   
        
        for idx in range(1, n-1):
            previous *= (1.0 + 1.0/(n-idx))
            
        return (1-previous) 


# January 01, 2023

'''

# Kunal Wadhwa

'''