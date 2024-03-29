# Question: https://leetcode.com/problems/maximum-subarray/
# Medium
class Solution:
    # O(n) Time and O(1) Space
    def maxSubArray(self, nums):
        dynamic_sum = nums[0]
        result = dynamic_sum
        
        for idx in range(1, len(nums)):
            dynamic_sum = max(dynamic_sum + nums[idx], nums[idx])
            result = max(result, dynamic_sum)
            
        return result

'''

# Kunal Wadhwa

'''