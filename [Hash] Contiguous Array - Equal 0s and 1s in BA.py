# Question: https://leetcode.com/problems/contiguous-array/
from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        def replace_zeroes(replace_with):
            for idx in range(len(nums)): nums[idx] = replace_with if nums[idx] == 0 else 1
                
        def find_max_length():
            hashmap = {0: -1}
            prefix_sum = 0
            result = 0
            
            for idx in range(len(nums)):
                prefix_sum += nums[idx]
                
                # if this prefix sum was already present in the hashmap
                # we added elements/nums which summed up to zero between the index at which this prefix sum was last present and the current index
                # and, if we summed up to zero, as we replaced zeroes with ones, there were equal number of ones and zeroes in this range
                # hence we update the result
                if prefix_sum in hashmap:
                    result = max(result, idx - hashmap[prefix_sum])
                else:
                    hashmap[prefix_sum] = idx
                    
            return result
        
        # to calculate prefix sum
        replace_zeroes(-1)
        return find_max_length()
    
# Kunal Wadhwa