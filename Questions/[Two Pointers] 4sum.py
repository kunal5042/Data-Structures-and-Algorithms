# Question: https://leetcode.com/problems/4sum/
# Medium
# 
from typing import Optional, List

class Solution:
    # O(n^3) Time and O(1) Extra Space
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruplets = set()
        
        # pointer 1
        for a in range(len(nums)):
            b = a + 1
            
            # pointer 2
            while b < len(nums):
                c, d = b+1, len(nums)-1
                
                # pointer 3 and 4
                while c < d:
                    _sum  = nums[a] + nums[b]
                    _sum += nums[c] + nums[d]
                    
                    if _sum == target:
                        quad = [nums[a], nums[b], nums[c], nums[d]]
                        quadruplets.add(tuple(quad))
                        
                        while c + 1 < len(nums) and nums[c] == nums[c+1]:
                            c += 1
                            
                    if _sum > target:
                        d -= 1
                    else:
                        c += 1
                        
                b += 1
                        
        return quadruplets
'''

# Kunal Wadhwa

'''