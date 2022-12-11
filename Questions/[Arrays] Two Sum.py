# Question: https://leetcode.com/problems/two-sum/
# Easy
# 
from typing import Optional, List
from collections import deque
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_elements_to_indices = {}
        
        # mapping nums in the nums array to their indices as a (key, value) pair
        for idx, num in enumerate(nums):
            if num in map_elements_to_indices:
                map_elements_to_indices[num].append(idx)
            else:
                map_elements_to_indices[num] = deque()
                map_elements_to_indices[num].append(idx)
                
                
            # Logic
            # target - x = y
            # if y is present in hash_map
            # means we found a pair x, y where x + y = target
                
            lookup = target - num
            
            if lookup in map_elements_to_indices:
                # we found the y
                # we can return the result, because the question states
                # that their exist only one such pair
                
                # we need to perform just one check before we return the result
                # that we are not using a duplicate element
                # for that
                indices = map_elements_to_indices[lookup]
                first_idx = indices.popleft()
                if first_idx != idx:
                    result = [idx, first_idx]
                    return result
                else:
                    # we were using a duplicate element and this can't form a valid pair
                    # add the popped index back for later use
                    indices.appendleft(first_idx)
            
        # we'll never reach this stage, because their exist one solution for every input
        # no pair was found, return False
        return [-1]
'''

# Kunal Wadhwa


'''