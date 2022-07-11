# Question: https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import Optional, List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Takes an integer list and a target sum
           Returns the minimum size of all subarrays whose sum is greater
           than equal to target
           """
        if nums[0] >= target: return 1
        
        start, end = 0, 1
        length = 1
        subarray_sum = nums[start]
        result = float('inf')

        while start < len(nums) and end < len(nums):
            subarray_sum += nums[end]

            if subarray_sum >= target:
                while start <= end and subarray_sum >= target:
                        result = min(result, end-start+1)
                        subarray_sum -= nums[start]
                        start += 1
                        continue
                        
                        break
                    
            end += 1
            
        return result if result != float('inf') else 0
    
    
# Algorithm
# Iterate over the given array
# And, at every iteration
# Keep track of window sum
# If window sum >= target
# as long as the above condition holds true, reduce the window size from left
# and keep updating the result

'''

# Kunal Wadhwa

'''