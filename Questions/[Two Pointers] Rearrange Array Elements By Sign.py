# Question: https://leetcode.com/problems/rearrange-array-elements-by-sign/
# Medium
# Easier than it looks
from typing import Optional, List

class Solution:
    # O(n) TIme and O(1) Space
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive, negative = 0, 0
        modified = []
        
        for idx in range(len(nums)):
            if idx % 2 == 0:
                
                while positive < len(nums) and nums[positive] < 0:
                    positive += 1
                modified.append(nums[positive])
                # currently points to positive
                # hence shift
                positive += 1
            
            else:
                
                while negative < len(nums) and nums[negative] > 0:
                    negative += 1
                modified.append(nums[negative])
                # currently points to negative
                # hence shift
                negative += 1
                
        return modified
'''

# Kunal Wadhwa

'''