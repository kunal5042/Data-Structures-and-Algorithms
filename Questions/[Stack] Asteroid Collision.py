# Question: https://leetcode.com/problems/asteroid-collision/
# Medium
#
from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for idx in range(len(asteroids)):
            if asteroids[idx] > 0:
                stack.append(asteroids[idx])
                
            else:
                while len(stack) != 0 and stack[~0] > 0 and stack[~0] < abs(asteroids[idx]):
                    stack.pop()
                    
                if len(stack) == 0 or stack[~0] < 0:
                    stack.append(asteroids[idx])
                    
                if stack[~0] == - asteroids[idx]:
                    stack.pop()
                    
        return stack
'''

# Kunal Wadhwa

'''