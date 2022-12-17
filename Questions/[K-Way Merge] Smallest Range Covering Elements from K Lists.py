# Question: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# Hard
from typing import Optional, List
from heapq import heappush, heappop

class Solution:
    # O(n * log(m)) - where n is the total number of elements in all lists
    # and m refers to the total number of lists
    
    # O(m) time
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        maxheap = []
        minheap = []
        
        for _list_no, _list in enumerate(nums):
            heappush(minheap, (_list[0] , 0, _list_no))
            heappush(maxheap, (-_list[0], 0, _list_no))
            
        lower_bound = 0
        upper_bound = float('inf')
        
        # start with the 0th element of all lists
        # we take the minimum and maximum among these elements
        # this defines the current range
        # we try to minimize this range
        # by moving ahead one element in the list from which we obtained
        # the lower bound of this range
        # we keep track of the shortest range
        
        while True:
            min_value, min_idx, min_list_no = heappop(minheap)
            max_value, max_idx, max_list_no = heappop(maxheap)
            max_value *= -1
            
            # update the shortest range
            if max_value - min_value < upper_bound - lower_bound:
                upper_bound = max_value
                lower_bound = min_value
                
            # if range is equal, check the next updation criterion
            elif max_value - min_value == upper_bound - lower_bound:
                if min_value < lower_bound:
                    lower_bound = min_value
                    upper_bound = max_value
                    
            # if the list with lower bound is exhausted
            if len(nums[min_list_no]) == min_idx + 1:
                break
                
            # updating both heaps
            x = (nums[min_list_no][min_idx+1], min_idx+1, min_list_no)
            heappush(minheap, x)
            y = (-x[0], x[1], x[2])
            heappush(maxheap, y)
            heappush(maxheap, (-max_value, max_idx, max_list_no))
            
        return [lower_bound, upper_bound]


# December 17, 2022

'''

# Kunal Wadhwa

'''