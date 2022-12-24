# Question: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
# Medium
from typing import Optional, List

class Solution:
    # O(n * log(n)) time and O(1) space
    def shipWithinDays(self, weights: List[int], max_days: int) -> int:
        # the goal is to minimize the capacity of the ship
        # the idea is to find the maximum capacity of the ship
        # and then minimize this value
        
        def can_suffice(capacity) -> bool:
            (idx, days, total) = (0, 1, 0)
            while idx < len(weights) and days <= max_days:
                if total + weights[idx] > capacity:
                    days += 1
                    total = weights[idx]
                else:
                    total += weights[idx]
                idx += 1
            return idx == len(weights) and days <= max_days
        
        minimum_capacity = sum(weights)
        bare_min = max(weights)
        (low, high) = 0, minimum_capacity
        while low <= high:
            candidate = (low + high) // 2
            if candidate >= bare_min and can_suffice(candidate) is True:
                minimum_capacity = candidate
                high = candidate-1
            else:
                low = candidate+1
                
        return minimum_capacity


# December 24, 2022

'''

# Kunal Wadhwa

'''