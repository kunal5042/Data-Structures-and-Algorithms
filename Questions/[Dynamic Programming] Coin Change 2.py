# Question: https://leetcode.com/problems/coin-change-2/
# Medium
from typing import Optional, List

class Solution:
    # O(amount*coins) Time and O(amount) Space 
    def change(self, amount: int, coins: List[int]) -> int:
        ways = [0 for _ in range(amount+1)]
        
        # base-case
        ways[0] = 1
        
        # bottom-up dynamic-programming
        for coin in coins:
            for idx in range(1, amount+1):
                if coin <= idx:
                    ways[idx] += ways[idx-coin]
                    
        return ways[~0]
            
'''

# Kunal Wadhwa

'''