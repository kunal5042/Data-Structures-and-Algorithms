# Question: https://leetcode.com/problems/first-unique-character-in-a-string/

from typing import Optional, List

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # creates an ordered frequency map
        frequency = Counter(s)
                
        # because it's ordered, the first char with freq == 1 is our result
        for char, freq in frequency.items():
            if freq == 1:
                return s.index(char)
            
        # if we haven't returned the result yet, there is no valid index
        # hence the result is -1
        return -1
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''