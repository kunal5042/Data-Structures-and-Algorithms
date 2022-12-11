# Question: https://leetcode.com/problems/min-stack/
# Medium
from typing import Optional, List

class MinStack:
    
    # O(1) Time and O(n) Space
    
    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]
        
    # O(1) Time 
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(self.min_stack[~0], val))

    # O(1) Time
    def pop(self) -> None:
        if not self.empty():
            self.stack.pop()
            self.min_stack.pop()

    # O(1) Time
    def top(self) -> int:
        if not self.empty():
            return self.stack[~0]

    # O(1) Time
    def getMin(self) -> int:
        if len(self.min_stack) > 1:
            return self.min_stack[~0]
        
    # O(1) Time
    def empty(self) -> bool:
        return len(self.stack) == 0
'''

# Kunal Wadhwa

'''