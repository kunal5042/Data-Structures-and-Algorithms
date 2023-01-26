# Question: https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
# Medium
from typing import Optional, List

class Solution:
    # O(n*log(n)) time and O(n) space
    def maxCoins(self, piles: List[int]) -> int:
        maxheap = [-pile for pile in piles]
        heapify(maxheap)
        
        count = 0
        your_turn = False
        money = 0
        
        while count < len(piles)//3:
            amount = abs(heappop(maxheap))

            if your_turn is True:
                count += 1
                money += amount
            
            your_turn = not your_turn
            
        return money


# January 26, 2023

'''

# Kunal Wadhwa

'''