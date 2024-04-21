# Question: https://leetcode.com/problems/first-missing-positive/description/
# Hard

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # -2^31 <= nums[i] <= 2^31 - 1
        # goal: find first positive integer missing in nums
        # expected complexity: time O(n) and space O(1)

        # Algorithm
        # Replace Negative Numbers with 0:
        # Iterate through each number in the list.
        # If the number is negative, replace it with 0.
        #
        # Mark Visited Indices:
        # Iterate through each number in the list.
        # Take the absolute value of the number (ignoring signs).
        # If the absolute value is 0, skip to the next number.
        # Calculate the target index by subtracting 1 from the absolute value (since indices start from 0).
        # If the target index is within the range of the list:
        # If the number at the target index is 0, replace it with infinity (a placeholder).
        # If the number at the target index is positive, multiply it by -1 (to mark it as visited).
        #
        # Find First Positive Missing Integer:
        # Iterate through each number in the list along with its index.
        # If the number is non-negative (either 0 or positive), return its index plus 1 (since indices start from 0).
        # If no positive integer is found, return the next integer after the length of the list.

        n = len(nums)

        # Step 1: Replace negative numbers with 0
        for idx in range(n):
            if nums[idx] < 0:
                nums[idx] = 0
        

        # Step 2: Mark visited indices
        for idx in range(n):
            positive_integer = abs(nums[idx])
            if positive_integer == 0: continue
            target = positive_integer - 1
            if target < n:
                if nums[target] == 0:
                    nums[target] = float('inf')
                if nums[target] > 0:
                    nums[target] *= -1
        
        # Step 3: Find first positive missing integer
        for idx, num in enumerate(nums):
            if num >= 0:
                return idx + 1

        # If no positive integer found, return next integer
        return n + 1


# March 26, 2024

'''

# Kunal Wadhwa

'''