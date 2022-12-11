# Question: https://leetcode.com/problems/design-a-stack-with-increment-operation/
# Medium
from typing import Optional, List

class CustomStack:

    def __init__(self, max_size: int):
        self.stack = [0 for _ in range(max_size)]
        self.top = 0

    def push(self, x: int) -> None:
        if not self.full():
            self.stack[self.top] = x
            self.top += 1

    def pop(self) -> int:
        if not self.empty():
            self.top -= 1
            return self.stack[self.top]
        
        return -1

    def increment(self, k: int, val: int) -> None:
        k = len(self.stack) if k > len(self.stack) else k
        for idx in range(k):
            self.stack[idx] += val
    
    def empty(self) -> bool:
        return self.top == 0
    
    def full(self) -> bool:
        return self.top == len(self.stack)


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
'''

# Kunal Wadhwa

'''