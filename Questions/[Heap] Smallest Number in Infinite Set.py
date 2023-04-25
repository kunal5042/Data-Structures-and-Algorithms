# Question: https://leetcode.com/problems/smallest-number-in-infinite-set/
# Medium

from heapq import heappop, heappush

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [1, 2, 3, 4, 5]
        self.container = set()

    def popSmallest(self) -> int:
        if len(self.heap) == 1:
            for num in range(self.heap[0]+1, self.heap[0]+5):
                heappush(self.heap, num)
                
        smallest = heappop(self.heap)
        self.container.add(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.container:
            self.container.discard(num)
            heappush(self.heap, num)


# April 25, 2023

'''

# Kunal Wadhwa

'''