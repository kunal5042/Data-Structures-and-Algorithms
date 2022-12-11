# Question: https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Easy
from typing import Optional, List
import math

class Solution:
    # O(1) time and O(1) space
    def gcdOfStrings(self, s1: str, s2: str) -> str:
        return s1[:math.gcd(len(s1), len(s2))] if s1 + s2 == s2 + s1 else ''

# November 18, 2022

'''

# Kunal Wadhwa

'''