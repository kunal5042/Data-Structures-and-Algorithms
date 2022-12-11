# Question: https://leetcode.com/problems/is-subsequence/
# Easy

from typing import Optional, List

class Solution:
    # O(len(s)*len(t)) Time and O(len(s)*len(t)) Space
    # using dynamic-programming
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t) : return False
        if len(s) == 0     : return True
        if len(s) == len(t): return s == t
        
        len_subseq = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        
        for row in range(1, len(s)+1):
            for col in range(1, len(t)+1):
                if s[row-1] == t[col-1]:
                    len_subseq[row][col] = max(len_subseq[row][col-1],
                                               len_subseq[row-1][col-1]+1)
                else:
                    len_subseq[row][col] = len_subseq[row][col-1]
                    
        return len_subseq[~0][~0] == len(s)
    
    
    # O(n) time and O(1) Space
    # using two-pointers
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if len(s) == 0    : return True
        
        sidx = 0
        for tidx in range(len(t)):
            if t[tidx] == s[sidx]:
                sidx += 1
            if sidx == len(s): return True
            
        return False
    

            
            
'''

# Kunal Wadhwa

'''