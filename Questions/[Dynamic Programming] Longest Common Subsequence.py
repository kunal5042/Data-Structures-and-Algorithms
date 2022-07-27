# Question: https://leetcode.com/problems/longest-common-subsequence/

from typing import Optional, List

class Solution:
    # O(m*n) Time and Space: where n and m are the length of the two strings
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Based on Levenshtein distance
        
        lcs = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        
        for row in range(1, len(lcs)):
            for col in range(1, len(lcs[row])):
                if text1[row-1] == text2[col-1]:
                    lcs[row][col] = (1 + lcs[row-1][col-1])
                else:
                    lcs[row][col] = max(lcs[row-1][col], lcs[row][col-1])
        
        return lcs[~0][~0]
'''

# Kunal Wadhwa

'''