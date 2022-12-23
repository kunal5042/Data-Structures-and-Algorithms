# Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Medium
from typing import Optional, List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo: dict = {}
            
        def maximize(idx:int, can_buy:bool):
            if idx >= len(prices):
                return 0
            
            if (idx, can_buy) in memo:
                return memo[(idx, can_buy)]
            
            cooldown = maximize(idx+1, can_buy)
            if can_buy is True:
                bought = maximize(idx+1, not can_buy) - prices[idx]
                memo[(idx, can_buy)] = max(bought, cooldown)
            else:
                sold = maximize(idx+2, not can_buy) + prices[idx]
                memo[(idx, can_buy)] = max(sold, cooldown)
                
            return memo[(idx, can_buy)]
        
        return maximize(0, True)


# December 23, 2022

'''

# Kunal Wadhwa

'''