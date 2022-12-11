# Question: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# Medium
# To Do: Implement tabulation
from typing import Optional, List

class Solution:
    # memoization
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target < n: return 0

        total_dies = n
        faces = k
        memo  = {}
        
        def roll_one_die(running_sum, dies_available):
            if dies_available == 0:
                if running_sum == 0:
                    return 1
                return 0
            
            if (running_sum, dies_available) in memo:
                return memo[(running_sum, dies_available)]
            
            ways = 0
            for face_value in range(1, faces+1):
                if running_sum - face_value <= target:
                    # new running sum
                    nrs = running_sum - face_value
                    # updated dies count
                    udc = dies_available - 1
                    
                    memo[(nrs, udc)] = roll_one_die(nrs, udc)
                    ways += memo[(nrs, udc)]
                    
            return ways
        
        return roll_one_die(target, total_dies) % (10**9 + 7)
'''

# Kunal Wadhwa

'''