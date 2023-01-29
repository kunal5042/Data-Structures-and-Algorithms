# Question: https://leetcode.com/problems/shuffle-an-array/
# Medium
from typing import Optional, List

import random
class Solution:

    def __init__(self, nums: List[int]):
        # cache
        self.array = nums
        self.permutations = []
        # store all
        # gives TLE
        # self.generate_permutations([], self.array)

    def reset(self) -> List[int]:
        return self.array

    def shuffle(self) -> List[int]:
        # equal possibility
        # index = random.randint(0, len(self.permutations)-1)
        # return self.permutations[index]
        
        # above solutions gives TLE
        # optimised approach using
        # FISHER-YATES ALGORITHM
        permutation = self.array.copy()
        for idx in range(len(self.array)):
            jdx = random.randint(0, len(self.array)-1)
            permutation[idx], permutation[jdx] = \
            permutation[jdx], permutation[idx]
            
        return permutation
        
    def generate_permutations(self, current, remaining):
        if len(current) == len(self.array):
            self.permutations.append(current.copy())
            return
        
        for idx in range(len(remaining)):
            current.append(remaining[idx])
            self.generate_permutations(current, remaining[:idx] + remaining[idx+1:])
            current.pop()




# January 29, 2023

'''

# Kunal Wadhwa

'''