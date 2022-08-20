# Question: https://leetcode.com/problems/search-insert-position/
# Easy
# Binary Search!
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            middle = (left + right ) // 2
            
            if nums[middle] == target:
                return middle
            
            if nums[middle] > target:
                right = middle -1
                
            else:
                left = middle + 1
                
        return left
        
# Kunal Wadhwa
