# Question: https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        
        hash   = set(nums)
        result = 0

        for num in nums:
            
            if (num-1) not in hash:
                target, current = num, 0

                while True:
                    if target in hash:
                        target  += 1
                        current += 1
                    else:
                        break

                result = max(result, current)
            
            
        return result
                
# Kunal Wadhwa