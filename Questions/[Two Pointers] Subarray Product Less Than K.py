# Question: https://leetcode.com/problems/subarray-product-less-than-k/
# Medium
# 
class Solution:
    # O(n) Time and O(1) Space
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            # Quick response for invalid k on product of positive numbers
            return 0
        
        left_sentry = 0

        num_of_subarray = 0
        product_of_subarry = 1

        # update right bound of sliding window
        for right_sentry in range( len(nums) ):

            product_of_subarry *= nums[right_sentry]

            # update left bound of sliding window
            while product_of_subarry >= k:
                product_of_subarry //= nums[left_sentry]
                left_sentry += 1

            # Note:
            # window size = right_sentry - left_sentry + 1

            # update number of subarrary with product < k
            num_of_subarray += right_sentry - left_sentry + 1

        return num_of_subarray
    
    def not_optimal_solution(self, nums: List[int], k: int) -> int:
        result = 0
        
        left, right = 0, 0
        curprod     = 1
        while left < len(nums):
            if right == len(nums):
                left  += 1
                right  = left
                
            if left >= len(nums) or right >= len(nums):
                break
            
            if left == right:
                if nums[left] < k:
                    curprod = nums[left]
                    result  += 1
                
                right += 1
                continue
            
            if curprod * nums[right] < k:
                result  += 1
                curprod *= nums[right]
                right   += 1
            else:
                left    += 1
                right   = left
                
        return result
    
# Kunal Wadhwa