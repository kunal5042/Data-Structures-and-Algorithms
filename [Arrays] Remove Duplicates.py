# Question: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):
        distinct_idx = 0
        for idx in range(1, len(nums)):
            if nums[distinct_idx] != nums[idx]:
                distinct_idx += 1
                nums[distinct_idx] = nums[idx]
                
        return distinct_idx + 1
    
    
    # Kunal Wadhwa
