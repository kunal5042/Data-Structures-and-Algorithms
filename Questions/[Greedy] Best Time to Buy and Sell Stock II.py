# Question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Medium
# To Do: Solve using DP ✅
from typing import Optional, List

class Solution:
    # Greedy Approach
    # O(n) Time and O(1) Space
    def maxProfit(self, prices: List[int]) -> int:
        profit  = 0
        hold = False
        
        for idx in range(len(prices)-1):
            if hold is True:
                if prices[idx] > bought:
                    profit += (prices[idx] - bought)
                    hold = False
                    
            if prices[idx] < prices[idx+1] and hold is False:
                bought = prices[idx]
                hold = True
                
        if hold is True and prices[~0] > bought:
            profit += (prices[~0] - bought)
            
        return profit
'''

# Kunal Wadhwa

'''