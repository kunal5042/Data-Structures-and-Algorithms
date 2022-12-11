# Question: https://leetcode.com/problems/online-stock-span/
# Medium
from typing import Optional, List

class StockSpanner:

    def __init__(self):
        self.len = 0
        self.stack = []

    # O(1) Time and O(n) Space
    def next(self, price: int) -> int:
        self.len += 1
        # stack is empty
        if len(self.stack) == 0:
            self.stack.append((price, self.len))
            return 1
        
        ele, pos = None, None
        while len(self.stack) != 0 and self.stack[~0][0] <= price:
            ele, pos = self.stack.pop()
            
        # greater than all
        if len(self.stack) == 0:
            self.stack.append((price, self.len))
            return self.len
        
        # loop didn't run
        if ele is None:
            self.stack.append((price, self.len))
            return 1
        
        # loop ran and stack is not empty
        self.stack.append((price, self.len))
        return self.len - self.stack[~1][1]

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

'''

# Kunal Wadhwa

'''