# Question: https://leetcode.com/problems/remove-element/

from typing import Optional, List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        overwrite_index = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[overwrite_index] = nums[idx]
                overwrite_index += 1
        return overwrite_index
# Question: https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums, val) -> int:
        def swap(x,y):
            nums[x], nums[y] = nums[y], nums[x]
            
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] != val:
                left += 1
                continue
            else:
                if nums[right] != val:
                    swap(left, right)
                    right -= 1
                    left  += 1
                    continue
                else:
                    right -= 1
        
        return left
    
# Kunal Wadhwa
'''

# Kunal Wadhwa

'''