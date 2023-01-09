# Question: https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(n) space
    def minimumCardPickup(self, cards: List[int]) -> int:
        indices = {}
        result = float('inf')
        
        for idx in range(len(cards)):
            card = cards[idx]
            if card in indices:
                result = min(result, idx - indices[card] + 1)
            indices[card] = idx
            
        return result if result != float('inf') else -1


# January 09, 2023

'''

# Kunal Wadhwa

'''