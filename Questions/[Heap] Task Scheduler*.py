# Question: https://leetcode.com/problems/task-scheduler/
# Medium
# Can revisit
from typing import Optional, List

from collections import Counter, deque
from heapq import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # goal: minimize idle time
        # each task takes one unit of time
        
        # keeps track of the time
        time = 0
        
        # for increased readability
        cooldown = n
        
        counts = Counter(tasks)
        heap   = [(-count) for task, count in counts.items()]
        
        # to get the most frequent task in O(1)
        heapify(heap)
        
        q = deque()
        
        while len(heap) or len(q):
            # at every iteration, one unit of time is passed
            time += 1

            if len(heap):
                taskfreq = heappop(heap)
            
                # this task has been processed and it's frequency can be decremented
                # as we are storing negative of frequency, to decrement it, we add 1 to it
                taskfreq += 1

                # this task can't be done till cool down is complete
                nextslot = time + cooldown

                if taskfreq != 0:
                    # this tasks needs to be done taskfreq times again and can be done again at time = nextslot
                    q.append([taskfreq, nextslot])
            
            
            # check if queue's first task's cooldown is complete
            # if it's complete, add it's count to the heap
            if len(q) and q[0][1] == time:
                heappush(heap, q.popleft()[0])
                
                
        return time

# Kunal Wadhwa
