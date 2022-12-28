# Question: https://leetcode.com/problems/minimum-size-subarray-sum/
# Medium

from typing import Optional, List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Takes an integer list and a target sum
           Returns the minimum size of all subarrays whose sum is greater
           than equal to target
           """
        if nums[0] >= target: return 1
        
        start, end = 0, 1
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
                    
            end += 1
            
        return result if result != float('inf') else 0
    
    
# Algorithm
# Iterate over the given array
# And, at every iteration
# Keep track of window sum
# If window sum >= target
# as long as the above condition holds true, reduce the window size from left
# and keep updating the result

# solved again, recently
class Solution:
    # O(n) time and O(1) space
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minimum_length = float('inf')
        window_start = -1
        subarray_sum = 0
        
        for idx in range(len(nums)):
            subarray_sum += nums[idx]

            while subarray_sum >= target:
                minimum_length = min(minimum_length, idx - window_start)
                subarray_sum -= nums[window_start+1]
                window_start += 1
                
        return minimum_length if minimum_length != float('inf') else 0
    
    # clarifying questions
    # can nums[i] be equal to zero?
    # can target be equal to zero?

'''

# Kunal Wadhwa

'''