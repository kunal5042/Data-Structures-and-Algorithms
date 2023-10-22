# Question: https://leetcode.com/problems/maximum-score-of-a-good-subarray/
# Hard

from typing import List

class Solution:
    # O(n) time and O(1) space
    def maximumScore(self, nums: List[int], k: int) -> int:
        # maximise the min in the subarray
        # maximise the length as second priority
        
        # must include nums[k]
        # starting from nums[k]
        # expand in both direction one at a time
        # decide in which direction to expand by finding the larger delta
        # keep track of the global maximum score 
        
        
        max_score = nums[k]
        cur_min = nums[k]
        length = 1
        left = k - 1
        right = k + 1
        
        while left > -1 or right < len(nums):
            delta_left = delta_right = 0
            
            if left > -1 and right < len(nums):
                if nums[left] < nums[right]:
                    delta_right = nums[right]
                    right += 1
                else:
                    delta_left = nums[left]
                    left -= 1
            
            elif left > -1:
                delta_left = nums[left]
                left -= 1
                
            else:
                delta_right = nums[right]
                right += 1
                    
            length += 1
            cur_min = min(cur_min, max(delta_right, delta_left))
            cur_score = (cur_min * length)
            max_score = max(
                max_score, cur_score
            )
            
        return max_score
                
            


# October 22, 2023

'''

# Kunal Wadhwa

'''