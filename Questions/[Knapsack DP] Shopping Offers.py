# Question: https://leetcode.com/problems/shopping-offers/
# Medium
from typing import Optional, List

class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], initial_needs: List[int]) -> int:
        memo = {}
        def helper(needs):
            lookup = str(needs)
            if lookup in memo: return memo[lookup]
            min_price = sum([price[idx]*needs[idx] for idx in range(len(needs))])
            
            for offer in special:
                if all([offer[i] <= needs[i] for i in range(len(needs))]):
                    updated_needs = [needs[i] - offer[i] for i in range(len(needs))]
                    min_price = min(min_price, offer[~0] + helper(updated_needs))
                    
            memo[str(needs)] = min_price
            return min_price
        
        return helper(initial_needs)
'''

# Kunal Wadhwa

'''