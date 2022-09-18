# Question: https://leetcode.com/problems/design-circular-queue/
# Medium
from typing import Optional, List

# Array Implementation
# All methods run in O(1) Time
# Code can be simplified if we keep track of the size of the queue
# I wanted to do it using just two pointers

class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [None for _ in range(k)]
        self.prear  = -1
        self.pfront = -1

    def enQueue(self, value: int) -> bool:
        if self.prear + 1 == len(self):
            if self.pfront > 0:
                self.prear = 0
                self.queue[self.prear] = value
                return True
            return False
        
        if self.prear < self.pfront:
            if self.pfront - self.prear - 1 > 0:
                self.prear += 1
                self.queue[self.prear] = value
                return True
            else:
                return False
            
        if self.pfront == -1:
            self.pfront = 0
            
        self.prear += 1
        self.queue[self.prear] = value
        return True
            
    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.queue[self.pfront] = None
            self.pfront += 1
            self.pfront %= len(self)
            
            if self.isEmpty():
                self.prear = -1
                self.pfront = -1
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.pfront]
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[self.prear]
        return -1

    def isEmpty(self) -> bool:
        if self.queue[self.pfront] is None:
            return True
        return False

    def isFull(self) -> bool:
        if self.prear == len(self) - 1:
            return True
        if self.pfront - self.prear == 1:
            return True
        return False
    
    def __len__(self):
        return len(self.queue)
'''

# Kunal Wadhwa

'''