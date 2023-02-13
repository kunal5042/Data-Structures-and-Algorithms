# Question: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
# Easy


class Solution:
    # O(1) time and O(1) space
    def countOdds(self, low: int, high: int) -> int:
        if low == high: return int(low % 2 != 0)
        low += 1 if low % 2 == 0 else 0
        answer = ((high - low) // 2) + 1
        return answer


# February 13, 2023

'''

# Kunal Wadhwa

'''