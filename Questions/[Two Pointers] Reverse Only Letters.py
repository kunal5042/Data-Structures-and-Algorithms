# Question: https://leetcode.com/problems/reverse-only-letters/
# Easy
from typing import Optional, List
import string
class Solution:
    # O(n) time and O(1) space
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s)-1
        alpha = set(string.ascii_lowercase).union(set(string.ascii_uppercase))
        output = [char for char in s]
        
        while left < right:
            if s[left] in alpha and s[right] in alpha:
                output[left] = s[right]
                output[right] = s[left]
                left += 1
                right -= 1
                
            if s[left] not in alpha:
                left += 1
                
            if s[right] not in alpha:
                right -= 1
                
        return "".join(output)


# November 21, 2022

'''

# Kunal Wadhwa

'''