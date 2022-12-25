# Question: https://leetcode.com/problems/next-permutation/
# Medium
# Try again :) -> Tried 😊
from typing import Optional, List

class Solution:
    # Brute-Force
    # O(n!) Time and O(n) Space
    def nextPermutation_BRUTE_FORCE(self, nums: List[int]) -> None:
        permutations = []
        def helper(current, remaining):
            if len(remaining) == 0: permutations.append(current)
                
            for idx, ele in enumerate(remaining):
                helper(current + [ele], remaining[:idx] + remaining[idx+1:])
                
        helper([], nums)
        permutations.sort()
        
        found_at = None
        for idx, perm in enumerate(permutations):
            if perm == nums:
                found_at = idx
                
        if found_at + 1 >= len(permutations):
            idx = 0
        else:
            idx = found_at + 1
            
        for jdx in range(len(nums)):
            nums[jdx] = permutations[idx][jdx]

    # O(n) Time and O(1) Space
    def nextPermutation(self, nums: List[int]) -> None:
        def swap(x, y):
            nums[x], nums[y] = nums[y], nums[x]
        
        def reverse(start, end):
            while start < end:
                swap(start, end)
                start += 1
                end   -= 1
        
        def get_replacement(start):
            comparison, next_smallest_greater, index = \
            nums[start-1], nums[start], start
            
            for idx in range(start, len(nums)):
                if nums[idx] > comparison and nums[idx] <= next_smallest_greater:
                    next_smallest_greater = nums[idx]
                    index = idx
            
            return index
        
        if len(nums) == 1: return
        
        need_to_sort = True
        for idx in reversed(range(1, len(nums))):
            if nums[idx-1] < nums[idx]:
                need_to_sort = False
                swap_with = get_replacement(idx)
                print(swap_with)
                swap(idx-1, swap_with)
                reverse(idx, len(nums)-1)
                break
                
        if need_to_sort: nums.sort()

    # O(n) time and O(1) space
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for idx in range(len(nums)-1, 0, -1):
            if nums[idx] > nums[idx-1]:
                # find just larger than nums[idx-1]
                jdx = idx
                while jdx < len(nums) and nums[jdx] > nums[idx-1]:
                    jdx += 1
                    
                # swapping nums[idx-1] with the number just larger
                # in the right partition
                nums[jdx-1], nums[idx-1] = nums[idx-1], nums[jdx-1]
                
                # reverse
                left, right = idx, len(nums)-1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left, right = left + 1, right - 1
                return
        nums.sort()
        
    # O(n) time and O(1) space
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        jdx, idx = len(nums)-2, len(nums)-1
        while jdx >= 0 and nums[jdx] >= nums[idx]:
            jdx, idx = jdx-1, idx-1
            
        if jdx < 0:
            nums.sort()
            return
        
        while idx < len(nums) and nums[idx] > nums[jdx]: idx += 1
        nums[jdx], nums[idx-1] = nums[idx-1], nums[jdx]
        
        left, right = jdx + 1, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

        return 
    
'''

# Kunal Wadhwa

'''