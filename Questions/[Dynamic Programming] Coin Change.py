# Question: https://leetcode.com/problems/coin-change/
# Medium
from typing import Optional, List

class Solution:
    def coinChange(self, coins: list[int], target: int) -> int:
        def helper(coins, target, count=0):
            # target value became negative implies that we couldn't deduct coins that sum upto target
            # but the sum of coins used is more than the target, hence this combination can't be used
            # return infinite, so that this count value is discarded
            if target < 0:
                return float('inf')

            # we deducted count number of coins from initial target and these count coins sum upto target
            # so, this current count value is a possible solution,
            # hence return it
            if target == 0:
                return count

            result = float('inf')

            # this loop will try every combination
            # at every iteration, we will have different count and target value to a new call
            # And, every call will have another loop with len(coins) call
            # these calls will start returning once we reach base condition
            # which will give us the number of coins used to reach target
            # we will keep track of minimum of these results        
            for coin in coins:
                result = min(result, helper(coins, target-coin, count+1))

            # And, return the minimum of all the counts
            return result

        answer = helper(coins, target)
        return answer if answer != float('inf') else -1

    # bottom-up dynamic programming
    # O(n*target) Time and O(target) Space
    def coinChange(self, coins: list[int], target: int) -> int:
        dp = [float('inf') for _ in range(target+1)]
        # base-case
        dp[0] = 0
        
        for amount in range(target+1):
            for denom in coins:
                if denom <= amount:
                    dp[amount] = min(dp[amount-denom]+1, dp[amount])
                    
        return dp[target] if dp[target] != float('inf') else -1
'''

# Kunal Wadhwa

'''