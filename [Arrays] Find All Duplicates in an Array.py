# Question: https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = list()
        
        for number in nums:
            
            idx = abs(number) - 1
            
            if nums[idx] < 0:
                result.append(abs(number))
                
            else:
                nums[idx] = -1 * nums[idx]
                
                
        return result
    
# Kunal Wadhwa