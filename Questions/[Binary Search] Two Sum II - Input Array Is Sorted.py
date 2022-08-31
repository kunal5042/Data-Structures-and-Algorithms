# Question: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Medium
from typing import Optional, List

class Solution:
    # O(log(n)) Time and O(1) Space
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        
        while left < right:
            _sum = nums[left] + nums[right]
            
            if _sum == target: return [left+1, right+1]
            
            if _sum > target:
                right -= 1
                
            else:
                left  += 1
        
        return [-1,-1]

'''

# Kunal Wadhwa

'''