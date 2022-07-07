# Question: https://leetcode.com/problems/longest-palindrome/

from typing import Optional, List

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        frequencies = Counter(s)
        
        odd    = False
        result = 0
        
        for freq in frequencies.values():
            if freq % 2 != 0:
                odd = True
                
            result += (freq // 2) * 2
            
        return result if odd is False else result + 1
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''