# Question: https://leetcode.com/problems/design-a-number-container-system/
# Medium
from typing import Optional, List

from heapq import heappop, heappush
class NumberContainers:

    def __init__(self):
        self.indices = {}
        self.numbers = defaultdict(list)

    # O(log(len(self.numbers[number]))) Time
    def change(self, index: int, number: int) -> None:
        self.indices[index] = number
        # insert index in the respective heap
        heappush(self.numbers[number], index)

    # O(len(self.numbers[number]) * log(len(self.numbers[number]))) Time
    def find(self, number: int) -> int:
        # number not present
        if number not in self.numbers: return -1
        
        while len(self.numbers[number]) > 0 and self.indices[self.numbers[number][0]] != number:
            heappop(self.numbers[number])
            
        # if heap is not empty that means root of heap is our resultant index
        return self.numbers[number][0] if len(self.numbers[number]) != 0 else -1
'''

# Kunal Wadhwa

'''