# Question: https://leetcode.com/problems/maximum-score-of-a-good-subarray/
# Hard
# Enjoyed solving it
from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def maximumScore(self, nums: List[int], k: int) -> int:
        max_score = nums[k]
        
        left   = k - 1
        right  = k + 1
        minima = nums[k]
        length = 1
        
        while left >= 0 or right < len(nums):
            while left >= 0 and right < len(nums):
                length += 1
                
                if nums[left] > nums[right]:
                    minima = min(minima, nums[left])
                    max_score = max(max_score, length * minima)
                    left -= 1
                else:
                    minima = min(minima, nums[right])
                    max_score = max(max_score, length * minima)
                    right += 1
                    
                    
            while left >= 0:
                length += 1
                minima = min(minima, nums[left])
                max_score = max(max_score, length * minima)
                left -= 1
                    
            while right < len(nums):
                length += 1
                minima = min(minima, nums[right])
                max_score = max(max_score, length * minima)
                right += 1
                
        return max_score
                
'''

# Kunal Wadhwa

'''