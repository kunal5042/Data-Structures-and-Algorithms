# Question: https://leetcode.com/problems/longest-common-subsequence/
# Medium

from typing import Optional, List

class Solution:
    # O(2^(m+n)) time
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longest = [0]
            
        def helper(idx1, idx2, length):
            longest[0] = max(longest[0], length)

            if idx1 == len(text1) or idx2 == len(text2):
                return

            # explore this path, as it will maximize the length
            if text1[idx1] == text2[idx2]:
                helper(idx1+1, idx2+1, length+1)
            else:
                # explore other paths
                helper(idx1+1, idx2  , length)
                helper(idx1  , idx2+1, length)
            return
        
        helper(0, 0, 0)
        return longest[0]
    
    # O(m*n) time: where n and m are the length of the two strings
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        # tail-recursion
        def helper(idx1, idx2):
            if idx1 == len(text1) or idx2 == len(text2):
                return 0
            
            # memoization-optimization
            if (idx1, idx2) in memo: return memo[(idx1, idx2)]

            if text1[idx1] == text2[idx2]:
                memo[(idx1, idx2)] = 1 + helper(idx1+1, idx2+1)
                
            else:
                memo[(idx1, idx2)] = max(
                    helper(idx1+1, idx2), 
                    helper(idx1  , idx2+1)
                )
            
            return memo[(idx1, idx2)]
        
        return helper(0, 0)

    # O(m*n) time and space: where n and m are the length of the two strings
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