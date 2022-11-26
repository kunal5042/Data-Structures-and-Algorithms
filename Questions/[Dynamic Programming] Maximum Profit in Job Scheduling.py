# Question: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# Hard
from typing import Optional, List

class Solution:
    # O(2**n) time
    def jobScheduling(self, start_time: List[int], end_time: List[int], profit: List[int]) -> int:
        jobs = []
        for idx in range(len(start_time)):
            jobs.append([start_time[idx], end_time[idx], profit[idx]])
            
        jobs.sort()
        start_time = [jobs[idx][0] for idx in range(len(jobs))]
        
        @cache
        # binary search and dynamic programming memoization
        def maximum_profit(idx):
            if idx == len(start_time):
                return 0
            
            jdx = bisect_left(start_time, jobs[idx][1])
            return max(jobs[idx][2] + maximum_profit(jdx), maximum_profit(idx+1))
        
        return maximum_profit(0)


# November 26, 2022

'''

# Kunal Wadhwa

'''