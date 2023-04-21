# Question: https://leetcode.com/problems/profitable-schemes/
# Hard

from functools import cache
from typing import List

class Solution:
    # O(len(group) * members_available * min_profit) time and space
    def profitableSchemes(self, n: int, min_profit: int, group: List[int], profit: List[int]) -> int:
        # Define a variable called mod and set its value to 10^9 + 7
        mod = 10**9 + 7

        @cache
        def rob(idx, members, running_profit):
            # If there are no members or if we have reached the end of the group list, check if the running profit is greater than or equal to the minimum profit
            if members < 1 or idx >= len(group):
                if running_profit >= min_profit:
                    return 1
                return 0

            ways = 0

            # If we have enough members to include the current group, then calculate the ways
            if members >= group[idx]:
                # We take minimum of min_proft and running_profit + profit[idx] to reduce the states and efficiently memoize
                ways += rob(idx + 1, members - group[idx], min(min_profit, running_profit + profit[idx]))

            # Calculate the ways if we exclude the current group
            ways += rob(idx + 1, members, running_profit)

            # Return the number of ways modulo mod
            return ways % mod

        return rob(0, n, 0)

        


# April 21, 2023

'''

# Kunal Wadhwa

'''