# Question: https://leetcode.com/problems/partition-equal-subset-sum/
# Medium

from typing import Optional, List

class Solution:
    # Recursive
    # O(2^n) Time and O(n) Space
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1: return False
        
        possible = [False]
        memo = {}
        
        def make_partitions(idx, part1, part2):
            if possible[0] is True: return
            
            if idx == len(nums):
                if sum(part1) == sum(part2):
                    possible[0] = True
                    return True
                return False
            
            current_ele = nums[idx]
            left =  make_partitions(idx + 1, part1 + [current_ele], part2.copy())
            if left is True: return True
            right = make_partitions(idx + 1, part1.copy(), part2 + [current_ele])
            
            return True if any([left, right]) else False
        
        make_partitions(0, [], [])
        return possible[0]
    
    # Recursive with Memoization
    # O(2^n) Time and O(n) Space
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) == 1: return False
        
        possible = [False]
        memo = {}
        
        def make_partitions(idx, part1, part2):
            if possible[0] is True: return
            sum_part1 = sum(part1)
            sum_part2 = sum(part2)
            if (idx, sum_part1, sum_part2) in memo:
                return memo[(idx, sum_part1, sum_part2)]
            if (idx, sum_part2, sum_part1) in memo:
                return memo[(idx, sum_part2, sum_part1)]
            
            if idx == len(nums):
                if sum_part1 == sum_part2:
                    possible[0] = True
                    return True
                return False
            
            current_ele = nums[idx]
            left = make_partitions(idx + 1, part1 + [current_ele], part2.copy())
            right = make_partitions(idx + 1, part1.copy(), part2 + [current_ele])
            
            memo[(idx, sum_part1+current_ele, sum_part2)] = left
            memo[(idx, sum_part1, sum_part2+current_ele)] = right
            memo[(idx, sum_part1, sum_part2)] = True if any([left, right]) else False
            
            return memo[(idx, sum_part1, sum_part2)]
        
        make_partitions(0, [], [])
        return possible[0]
    
    
    # Dynamic-Programming
    def canPartition(self, nums: List[int]) -> bool:
        dp = set([0])
        _sum = sum(nums)
        if _sum % 2 != 0: return False
        
        target = _sum // 2
        
        for idx in reversed(range(len(nums))):
            updates = set()
            for ele in dp:
                subset_sum = ele + nums[idx]
                # if subset_sum == target: return True
                updates.add(subset_sum)
                
            dp = dp.union(updates)
            
        return True if target in dp else False
                	
'''

# Kunal Wadhwa

'''
