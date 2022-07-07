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
