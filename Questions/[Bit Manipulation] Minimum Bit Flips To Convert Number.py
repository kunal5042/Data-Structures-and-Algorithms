# Question: https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
# Easy
from typing import Optional, List

class Solution:
    # O(max(bin(start), bin(goal)))
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal  = bin(goal)[2:]
        
        if len(start) > len(goal):
            leading_zeroes = ''
            for _ in range(len(start) - len(goal)):
                leading_zeroes += '0'
                
            goal = leading_zeroes + goal
            
        elif len(goal) > len(start):
            leading_zeroes = ''
            for _ in range(len(goal) - len(start)):
                leading_zeroes += '0'
                
            start = leading_zeroes + start
            
        flips = 0
        for idx in range(len(start)):
            if start[idx] != goal[idx]:
                flips += 1
                
        return flips
    
    
    # Using Bit Manipulation
    def minBitFlips(self, start: int, goal: int) -> int:
        return (start^goal).bit_count()
        
'''

# Kunal Wadhwa

'''