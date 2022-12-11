# Question: https://leetcode.com/problems/get-maximum-in-generated-array/
# Easy

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        
        cache = {0:0, 1:1}
        
        idx, count = 1, 0
        even = True
        
        while count < n-1:
            if even is True:
                cache[2*idx] = cache[idx]
            else:
                cache[(2*idx)+1] = cache[idx] + cache[idx+1]
                idx += 1
                
            count += 1
            even = not even
            
        return max(cache.values())
    
    # O(n//2) Time and O(n) Space
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        
        nums    = [0 for _ in range(n+1)]
        nums[1] = 1
        result  = 1
        
        for idx in range(1, (n+1)//2):
            nums[2*idx] = nums[idx]
            nums[2*idx+1] = nums[idx] + nums[idx+1]
            result = max(nums[2*idx+1], nums[2*idx], result)
            
        return result
'''

# Kunal Wadhwa

'''