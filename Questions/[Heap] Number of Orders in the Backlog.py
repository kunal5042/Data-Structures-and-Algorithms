# Question: https://leetcode.com/problems/number-of-orders-in-the-backlog/description/
# Medium

from heapq import heappop, heappush
from typing import List

class Solution:
    # O(n * log(n)) time and O(n) space
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        max_heap = []
        min_heap = []

        for price, quantity, order_type in orders:
            if order_type == 1: heappush(min_heap, [ price, quantity])
            if order_type == 0: heappush(max_heap, [-price, quantity])

            while max_heap and min_heap and min_heap[0][0] <= abs(max_heap[0][0]):
                sell_count = min_heap[0][1]
                buy_count  = abs(max_heap[0][1])

                if sell_count == buy_count:
                    heappop(min_heap)
                    heappop(max_heap)
                    continue

                if sell_count < buy_count:
                    heappop(min_heap)
                    max_heap[0][1] -= sell_count
                else:
                    heappop(max_heap)
                    min_heap[0][1] -= buy_count

        result  = sum([x[1] for x in min_heap])
        result += sum([x[1] for x in max_heap])
        return result % (1000000007)


# June 10, 2023

'''

# Kunal Wadhwa

'''