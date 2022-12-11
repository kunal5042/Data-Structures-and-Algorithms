# Question: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
# Medium
from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def minCost(self, colors: str, needed_time: List[int]) -> int:
        if len(colors) == 1: return 0
        
        time = 0
        removal_time_for_prev = needed_time[0]
        previous = colors[0]
        for idx in range(1, len(colors)):
            
            # two balloons with same colors
            if colors[idx] == previous:
                time += min(needed_time[idx], removal_time_for_prev)
                removal_time_for_prev = max(needed_time[idx], removal_time_for_prev)
                
            else:
                # different balloons
                # no updation of required time
                previous = colors[idx]
                removal_time_for_prev = needed_time[idx]
                
        return time
    
    # Below two solutions are similar to the first one
    # All run in same asymptotic time complexity, but first one is the fastest
    
    # O(n) Time and O(1) Space
    # Greedy using Heap
    def minCost(self, colors: str, needed_time: List[int]) -> int:
        if len(colors) == 1: return 0
        
        time = 0
        heap = [needed_time[0]]
        previous = colors[0]
        for idx in range(1, len(colors)):
            if colors[idx] == previous:
                heappush(heap, needed_time[idx])
                time += heappop(heap)
                
            else:
                previous = colors[idx]
                heap = [needed_time[idx]]
                
        return time
    
    # O(n) Time and O(1) Space
    # Greedy using Stack
    def minCost(self, colors: str, needed_time: List[int]) -> int:
        if len(colors) == 1: return 0
        
        time = 0
        stack = [needed_time[0]]
        previous = colors[0]
        for idx in range(1, len(colors)):
            
            # two balloons with same colors
            if colors[idx] == previous:
                
                # faster to remove first one
                if stack[~0] < needed_time[idx]:
                    time += stack.pop()
                    stack.append(needed_time[idx])
                    
                else:
                    # faster to remove second one
                    time += needed_time[idx]
                
            else:
                # different balloons
                # no updation of required time
                # re-allocate stack
                previous = colors[idx]
                stack = [needed_time[idx]]
                
        return time
    

'''

# Kunal Wadhwa

'''