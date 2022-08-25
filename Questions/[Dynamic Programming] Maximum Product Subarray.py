# Question: https://leetcode.com/problems/maximum-product-subarray/
# Medium
from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def maxProduct(self, nums: List[int]) -> int:
        result = minimum = maximum = nums[0]
        
        for idx in range(1, len(nums)):
            if nums[idx] < 0:
                minimum, maximum = maximum, minimum
                
            minimum = min(nums[idx], nums[idx]*minimum)
            maximum = max(nums[idx], nums[idx]*maximum)
            result  = max(result, maximum)
            
        return result
# Question: https://leetcode.com/problems/maximum-product-subarray/

from typing import Optional, List

class Solution:
    def maxProduct(self, nums):
        """
        Returns the maximum of product of all subarrays
        
        Args:
            nums: List[int]
            
        Returns:
            maximum product: int
            
        """
        if len(nums) == 1: return nums[0]
        
        sub_max, sub_min = nums[0], nums[0]
        result = nums[0]
        
        for idx in range(1, len(nums)):
            if nums[idx] < 0:
                sub_max, sub_min = sub_min, sub_max
                
            sub_max = max(sub_max * nums[idx], nums[idx])
            sub_min = min(sub_min * nums[idx], nums[idx])
            
            result = max(sub_max, sub_min, result)

        return result
                
                
'''

# Kunal Wadhwa

''''''

# Kunal Wadhwa

'''