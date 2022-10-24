# Question: https://leetcode.com/problems/3sum-closest/
# Medium
from typing import Optional, List

class Solution:
    # O(n*n) Time and O(1) Space
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        result = float('inf')
        nums.sort()
        
        for idx in range(0, len(nums)-2):
            left, right = idx + 1, len(nums) - 1

            # two-pointers in the right partition
            while left < right:
                triplet_sum = nums[idx] + nums[left] + nums[right]
                current = abs(target - triplet_sum)
                closest = abs(target - result)
                
                # udpate result, if a closer sum is found
                if current < closest:
                    result = triplet_sum
                
                # get closer to the targer
                if triplet_sum > target:
                    right -= 1
                
                elif triplet_sum < target:
                    left += 1
                
                # small optimisation
                else:
                    return target
        
        return result
'''

# Kunal Wadhwa

'''