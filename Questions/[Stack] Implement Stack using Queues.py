# Question: https://leetcode.com/problems/implement-stack-using-queues/
# Easy
from typing import Optional, List

class Queue:
    def __init__(self):
        self.queue = deque()
        
    def enqueue(self, val):
        self.queue.append(val)
        
    def dequeue(self):
        if len(self) > 0:
            return self.queue.popleft()
        
    def __len__(self):
        return len(self.queue)
        
class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.enqueue(x)

    def pop(self) -> int:
        if len(self.queue) != 0:
            for _ in range(len(self.queue)-1):
                self.queue.enqueue(self.queue.dequeue())
            return self.queue.dequeue()

    def top(self) -> int:
        if len(self.queue) != 0:
            for _ in range(len(self.queue)-1):
                self.queue.enqueue(self.queue.dequeue())
            stack_top = self.queue.dequeue()
            self.queue.enqueue(stack_top)
            return stack_top

    def empty(self) -> bool:
        return len(self.queue) == 0
'''

# Kunal Wadhwa

'''