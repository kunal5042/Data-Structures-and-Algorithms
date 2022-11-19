# Question: https://leetcode.com/problems/arranging-coins/
# Easy
from typing import Optional, List

class Solution:
    # naive solution
    def arrangeCoins(self, n: int) -> int:
        start = 1
        output = 0
        
        while start <= n:
            n -= start
            output += 1
            start += 1
            
        return output
    
    # efficient solution based on binary-search
    def arrangeCoins(self, n: int) -> int:
        # k(k+1) // 2 <= n
        left = 0
        right = n
        while left <= right:
            k = (left + right) // 2
            
            curr = k *(k+1) // 2
            
            if curr == n: return k
            
            if curr < n:
                left = k + 1
            else:
                right = k - 1
            
        return right


# November 19, 2022

'''

# Kunal Wadhwa

'''