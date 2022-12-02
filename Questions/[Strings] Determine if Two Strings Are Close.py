# Question: https://leetcode.com/problems/determine-if-two-strings-are-close/
# Medium
from typing import Optional, List

class Solution:
    # O(n*log(n)) time and O(n) space
    def closeStrings(self, word1: str, word2: str) -> bool:
        # attain one from the other string
        # operation-1: swap any two existing characters
        # operation-2: transform every occurence of one existing character
        # into another existing character, and do the same with the
        # other character
        
        # base-condition
        if len(word1) != len(word2):
            return False
        
        _hash1 = {}
        _hash2 = {} 
        
        
        for idx in range(len(word1)):
            _hash1[word1[idx]] = _hash1.get(word1[idx], 0) + 1
            _hash2[word2[idx]] = _hash2.get(word2[idx], 0) + 1
            
        # intuition
        # if two string have same type of chars
        # and same type of frequencies
        # by applying operations 1 and 2, we can get one from the other
        freq1  = sorted(list(_hash1.values()))
        freq2  = sorted(list(_hash2.values()))
        chars1 = sorted(list(_hash1.keys()))
        chars2 = sorted(list(_hash2.keys()))
        
        return freq1 == freq2 and chars1 == chars2
        


# December 02, 2022

'''

# Kunal Wadhwa

'''