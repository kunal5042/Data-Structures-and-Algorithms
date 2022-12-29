# Question: https://leetcode.com/problems/single-threaded-cpu/
# Medium

from typing import Optional, List
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # maps time instant to the tasks which are available for processing at that time
        availability = defaultdict(list)
        # min heap that stores all the tasks that are available to process at this time
        available = []
        # hashset of all the time instants 
        times = set()
        # output of the program
        order = []
        
        for idx, (enqueue_time, process_time) in enumerate(tasks):
            availability[enqueue_time].append((process_time, idx))
            times.add(enqueue_time)
            
        # we want all time instants in reverse sorted order
        # so we can compare current time with last element in this array
        # can can remove the last element in O(1) time
        times = sorted(list(times), reverse=True)
        # starting with the smallest time value
        time = times[~0]
        
        # loop runs till all the available tasks are not processed
        while len(times) != 0 or len(available) != 0:
            # if the current time is greater or equal to earliest time instant
            # in the times array
            # it will take all the available tasks of all time instants that are smaller than current time and add them to the min-heap
            while len(times) != 0 and time >= times[~0]:
                x = times.pop()
                for process_time, idx in availability[x]:
                    heappush(available, (process_time, idx))
                
            # it is possible that  all tasks are processed 
            # which were available at or before current time instant
            # and that's why heap could be empty 
            if len(available) != 0:
                process_time, idx = heappop(available)
                time += process_time
                order.append(idx)
                
            # if the heap is empty and the times array is not
            # that states the next available tasks will be at the last element of the times array
            elif len(times) != 0:
                time = times[~0]
            
        return order


# December 29, 2022

'''

# Kunal Wadhwa

'''