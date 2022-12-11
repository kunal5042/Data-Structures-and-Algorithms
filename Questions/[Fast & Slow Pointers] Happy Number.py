# Question: https://leetcode.com/problems/happy-number/
# Easy
# Good one!
from typing import Optional, List

class Solution:
    # Using Floyd's Cycle Detection Algorithm
    def isHappy(self, n: int) -> bool:
        def sum_of_digits_squared(num):
            _sum = 0
            
            while num > 0:
                digit = num % 10
                _sum += (digit * digit)
                num = num // 10
                
            return _sum
        
        slow = fast = n
        
        while True:
            slow = sum_of_digits_squared(slow)
            fast = sum_of_digits_squared(fast)
            fast = sum_of_digits_squared(fast)
            if slow == fast: break
            
        if slow == 1: return True
        return False
            
    
    # Using Hash-Table
    def isHappy(self, n: int) -> bool:
        def sum_of_digits_squared(num):
            _sum = 0
            
            while num > 0:
                digit = num % 10
                _sum += (digit * digit)
                num = num // 10
                
            return _sum
        
        num = n
        visited = set()
        while True:
            if num in visited: return False
            if num == 1      : return True
            
            visited.add(num)
            num = sum_of_digits_squared(num)
            
        return
'''

# Kunal Wadhwa

'''