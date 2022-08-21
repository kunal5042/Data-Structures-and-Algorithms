# Question: https://leetcode.com/problems/permutations-ii/
# Medium
# Update counter for each call to generate unique paths
from typing import Optional, List

from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        result = []
        def permute(permutation):
            if len(permutation) == len(nums):
                result.append(permutation.copy())
                return
            
            for choice in counts:
                if counts[choice] > 0:
                    permutation.append(choice)
                    counts[choice] -= 1
                    permute(permutation)
                    counts[choice] += 1
                    permutation.pop()
                
        permute([])
        return result
'''

# Kunal Wadhwa

'''