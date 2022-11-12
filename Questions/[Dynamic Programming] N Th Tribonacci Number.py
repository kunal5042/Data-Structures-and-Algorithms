# Question: https://leetcode.com/problems/n-th-tribonacci-number/
# Easy

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    # dynamic-programming tabulation
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        
        tab = [None for _ in range(n+1)]
        tab[0] = 0
        tab[1] = tab[2] = 1
        
        for num in range(3, n+1):
            tab[num] = tab[num-1] + tab[num-2] + tab[num-3]
            
        return tab[~0]
'''

# Kunal Wadhwa

'''