# Question: https://leetcode.com/problems/custom-sort-string/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(n) space where n is the length of s
    def customSortString(self, order: str, s: str) -> str:
        available_chars = {}
        
        for char in s:
            if char not in available_chars:
                available_chars[char] = 0
            available_chars[char] += 1
            
        permutation = []
        for char in order:
            if char in available_chars:
                for _ in range(available_chars[char]):
                    permutation.append(char)

                del available_chars[char]
                
        for char, freq in available_chars.items():
            for _ in range(freq):
                permutation.append(char)
                
        return "".join(permutation)


# January 17, 2023

'''

# Kunal Wadhwa

'''