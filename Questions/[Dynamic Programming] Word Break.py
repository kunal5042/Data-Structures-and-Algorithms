# Question: https://leetcode.com/problems/word-break/
# Medium

from typing import Optional, List
from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s)+1)]
        dp[len(s)] = True
        
        for idx in reversed(range(len(s))):
            for word in wordDict:
                # can we compare?
                if (idx + len(word)) <= len(s) and s[idx: idx+len(word)] == word:
                    dp[idx] = dp[idx + len(word)]
                
                if dp[idx] is True: break
        
        return dp[0]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        
        def match(idx, word):
            jdx = 0
            while idx < len(s) and jdx < len(word) and s[idx] == word[jdx]:
                idx += 1
                jdx += 1
                
            return jdx == len(word)
           
        @cache
        def helper(idx):
            if idx == len(s):
                return True
            
            for word in words:
                if s[idx] == word[0] and idx + len(word) <= len(s):
                    if match(idx, word) is True:
                        if helper(idx+len(word)) is True:
                            return True
            return False
        
        return helper(0)
'''

# Kunal Wadhwa

'''