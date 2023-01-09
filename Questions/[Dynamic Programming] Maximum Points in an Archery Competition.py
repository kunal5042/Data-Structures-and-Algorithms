# Question: https://leetcode.com/problems/maximum-points-in-an-archery-competition/
# Medium
from typing import Optional, List

class Solution:
    # Read the description wrong
    # this code returns the maximum points which is the final answer
    # we need to return the array which led to the final answer
    def maximumBobPoints(self, num_arrows: int, alice_arrows: List[int]) -> List[int]:
        @cache
        def optimal_path(idx, arrows):
            if idx >= 12 or arrows == 0:
                return 0
            
            won = 0
            lost = 0
            if alice_arrows[idx] <= arrows:
                won = idx + optimal_path(idx+1, arrows-alice_arrows[idx]-1)
            
            lost += optimal_path(idx+1, arrows)
                
            return max(won, lost)
        
        return [optimal_path(0, num_arrows)]
    
    def maximumBobPoints(self, num_arrows: int, alice_arrows: List[int]) -> List[int]:
        @cache
        def optimal_path(idx, arrows):
            if idx >= 12 or arrows == 0:
                return 0
            
            won = 0
            lost = 0
            if alice_arrows[idx] < arrows:
                won = idx + optimal_path(idx+1, arrows-alice_arrows[idx]-1)
            
            lost += optimal_path(idx+1, arrows)
                
            return max(won, lost)
        
        result = [0 for _ in range(12)]
        remaining = num_arrows
        for idx in range(0, 12):
            if optimal_path(idx, remaining) != optimal_path(idx+1, remaining):
                result[idx] = alice_arrows[idx] + 1
                remaining -= alice_arrows[idx] + 1
        
        if remaining > 0:
            result[0] += remaining
        
        return result

        	


# January 09, 2023

'''

# Kunal Wadhwa

'''