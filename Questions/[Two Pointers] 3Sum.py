# Question: https://leetcode.com/problems/3sum/
# Medium
# Break it down into two sum problem
class Solution:
    "Optimal Solution: Two Pointer Approach"
    # O(n^2) Time and O(1) Space
    def threeSum(self, nums):
        nums.sort()
        result = list()
        for idx in range(len(nums)):
            # edge case
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
                
            left, right = idx + 1, len(nums)-1
            
            # updating left and right trying to close in on the target sum
            while left < right:
                triplet = [nums[idx], nums[left], nums[right]]
                triplet_sum = sum(triplet)
                
                if triplet_sum > 0:
                    right -= 1
                elif triplet_sum < 0:
                    left += 1
                else:
                    result.append(triplet)
                    left += 1
                    # Tricky part
                    # skipping over duplicates
                    # because array is sorted
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    
                    
        return result
    
    "Requires extra space: Using Hashing"
    # O(n^2) Time and O(n) Space
    def three_sum(self, nums):
        result = list()
        hash = {}
        
        for idx in range(len(nums)):
            hash[nums[idx]] = idx
        
        for idx in range(len(nums)):
            csum = nums[idx]
            for jdx in range(idx+1, len(nums)):
                hash_target = 0 - (csum + nums[jdx])
                if hash_target in hash and hash[hash_target] not in [idx, jdx]:
                    triplet = sorted([nums[idx], nums[jdx], hash_target])
                    if triplet not in result:
                        result.append(triplet)
                    
        return result
    
# Kunal Wadhwa