# Question: https://leetcode.com/problems/summary-ranges/description/
# Easy

from typing import List

class Solution:
    def __init__(self):
        self.summary = []

    # O(1) time and O(1) space
    def add_to_summary(self, nums, start, end):
        if start < 0 or end >= len(nums):
            return

        if start != end:
            self.summary.append(f"{nums[start]}->{nums[end]}")
        else:
            self.summary.append(f"{nums[start]}")

    # O(n) time and O(1) space
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = end = len(nums) - 1
        for idx in range(len(nums)-2, -1, -1):
            if nums[idx+1] - nums[idx] == 1:
                start = idx
                continue

            self.add_to_summary(nums, start, end)
            start = end = idx

        self.add_to_summary(nums, start, end)
        self.summary.reverse()
        return self.summary


# June 12, 2023

'''

# Kunal Wadhwa

'''