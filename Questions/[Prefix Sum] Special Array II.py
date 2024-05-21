# Question: https://leetcode.com/problems/special-array-ii/description/
# Medium

from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        prefix = [0 for _ in range(len(nums))]
        answer = []

        for idx in range(1, len(nums)):
            prefix[idx] = prefix[idx-1]

            if nums[idx] % 2 == nums[idx-1] % 2:
                prefix[idx] += 1

        for start, end in queries:
            answer.append(
                prefix[end] - prefix[start] == 0
            )

        return answer


# May 21, 2024

'''

# Kunal Wadhwa

'''