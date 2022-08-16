# Question: https://leetcode.com/problems/daily-temperatures/

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic-increasing
        stack = []
        
        temps = temperatures
        answer = [None] * len(temps)
        
        # to check if stack is empty
        empty = lambda x: len(x) == 0
        
        for idx in reversed(range(len(temps))):
            while not empty(stack) and temps[stack[~0]] <= temps[idx]:
                stack.pop()
                
            if not empty(stack):
                answer[idx] = stack[~0] - idx
            else:
                answer[idx] = 0
                
            stack.append(idx)
                
        return answer
                
'''

# Kunal Wadhwa

'''