# Question: https://leetcode.com/problems/stock-price-fluctuation/
# Medium
from typing import Optional, List

class StockPrice:
    def __init__(self):
        self.hash = {}
        self.latest = -1
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.latest = max(self.latest, timestamp)
        self.hash[timestamp] = price
        heappush(self.min_heap, (price,  timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        return self.hash[self.latest]

    def maximum(self) -> int:
        while self.hash[self.max_heap[0][1]] != abs(self.max_heap[0][0]):
            heappop(self.max_heap)
        return abs(self.max_heap[0][0])
    
    def minimum(self) -> int:
        while self.hash[self.min_heap[0][1]] != self.min_heap[0][0]:
            heappop(self.min_heap)
        return self.min_heap[0][0]


# January 13, 2023

'''

# Kunal Wadhwa

'''