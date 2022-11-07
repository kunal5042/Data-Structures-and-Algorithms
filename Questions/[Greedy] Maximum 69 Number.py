# Question: https://leetcode.com/problems/maximum-69-number/
# Easy
from typing import Optional, List

class Solution:
    def maximum69Number (self, num: int) -> int:
        output, can_change = 0, True
        digits = []
        
        while num != 0:
            digits.append(num%10)
            num //= 10
            
        for idx in reversed(range(len(digits))):
            if digits[idx] == 6 and can_change:
                can_change = not can_change
                digits[idx] = 9
            
            output += (digits[idx]*(10**idx))
            
        return output
'''

# Kunal Wadhwa

'''