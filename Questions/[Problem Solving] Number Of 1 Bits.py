# Question: https://leetcode.com/problems/number-of-1-bits/
# Easy
# To Do: Solve using Bit Manipulation
from typing import Optional, List

from collections import Counter
class Solution:
    def hammingWeight(self, n: int) -> int:
        return Counter(bin(n)[2:])['1']
'''

# Kunal Wadhwa

'''