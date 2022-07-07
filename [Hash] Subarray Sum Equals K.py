# Question: https://leetcode.com/problems/subarray-sum-equals-k/

'''O(n) Time'''
class Solution:
    def subarraySum(self, nums, k):
        hashmap   = dict()
        prefixsum = 0
        result    = 0
        
        for idx in range(len(nums)):
            prefixsum += nums[idx]
            if prefixsum - k in hashmap:
                result += hashmap[prefixsum - k]
                
            if prefixsum == k:
                result += 1
                
                
            hashmap[prefixsum] = hashmap.get(prefixsum, 0) + 1
        return result
    
# Kunal Wadhwa