# Question: https://leetcode.com/problems/sort-colors/submissions/

from collections import Counter
class Solution:
    def sortColors(self, nums) -> None:
        def swap(x, y):
            nums[x], nums[y] = nums[y], nums[x]
            
        # using three pointers
        zero_pointer = 0
        two_pointer  = len(nums)-1
        one_pointer  = 0
        
        while one_pointer <= two_pointer:
            if nums[one_pointer] == 0:
                swap(zero_pointer, one_pointer)
                zero_pointer += 1
                one_pointer  += 1
                
            elif nums[one_pointer] == 2:
                swap(two_pointer, one_pointer)
                two_pointer -= 1
                
            else:
                one_pointer += 1
            

            
    def sort_colors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        
        idx = 0
        for _ in range(counts[0]):
            nums[idx] = 0
            idx += 1
            
        for _ in range(counts[1]):
            nums[idx] = 1
            idx += 1
            
        for _ in range(counts[2]):
            nums[idx] = 2
            idx += 1
            
        return
        

            
        