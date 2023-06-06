# Question: https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
# Easy

from typing import List

class Solution:
    # O(n) time and O(n) space
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        min_val = float('inf')
        max_val = float('-inf')

        for ele in arr:
            min_val = min(ele, min_val)
            max_val = max(ele, max_val)

        if max_val - min_val == 0:
            return True

        if (max_val - min_val) % (len(arr)-1) != 0:
            return False

        diff = (max_val - min_val) // (len(arr)-1)
        numbers = set()

        for ele in arr:
            if (ele - min_val) % diff:
                return False
            numbers.add(ele)

        return len(numbers) == len(arr)


# June 06, 2023

'''

# Kunal Wadhwa

'''