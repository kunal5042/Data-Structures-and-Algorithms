# Question: https://leetcode.com/problems/car-fleet/

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(pos, spd) for pos, spd in zip(position, speed)]
        pairs.sort()
        
        stack = []
        for idx in reversed(range(len(pairs))):
            pos, spd = pairs[idx]
            # calculate the time at which this car reaches dest
            dest_time = (target - pos) / spd
            stack.append(dest_time)
            if len(stack) >= 2:
                # if this car's time at which it reaches dest
                # is smaller than the dest time of previous stack top
                # that means, they intersect and become a car fleet
                if stack[~0] <= stack[~1]:
                    stack.pop()
     
        # return car fleets
        return len(stack)
            
            
'''

# Kunal Wadhwa

'''