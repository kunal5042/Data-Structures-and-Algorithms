# Question: https://leetcode.com/problems/next-permutation/
# Medium
# Try again :)
from typing import Optional, List

class Solution:
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
'''

# Kunal Wadhwa

'''