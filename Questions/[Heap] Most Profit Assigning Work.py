# Question: https://leetcode.com/problems/most-profit-assigning-work/description/?envType=list&envId=oavyeqsc
# Medium

from heapq import heapify, heappop
from typing import List

class Solution:
    def maxProfitAssignment(self, difficulties: List[int], profits: List[int], workers: List[int]) -> int:
        # difficulty -> profit
        # one to many relationship between worker and job
        
        # goal:
        #   - maximise the profit
        #   - utilise all the workers

        # algorithm
        # couple the (profit, difficulty) together and store in a maxheap
        # sort the workers in decreasing order
        # traverse the sorted workers array
        # at each iteration check if the current worker's ability covers the max heap's highest profit difficulty
        # if yes add the profit to profits
        # else pop from the maxheap

        result = 0
        maxheap = []
        for (profit, difficulty) in zip(profits, difficulties):
            maxheap.append((-profit, difficulty))

        heapify(maxheap)
        workers.sort(reverse=True)

        for ability in workers:
            while len(maxheap) > 0 and maxheap[0][1] > ability:
                heappop(maxheap)

            if len(maxheap) > 0:
                result += abs(maxheap[0][0])

        return result


# April 01, 2024

'''

# Kunal Wadhwa

'''