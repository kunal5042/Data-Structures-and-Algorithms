# Question: https://leetcode.com/problems/word-break/
# Medium

from typing import Optional, List

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
'''

# Kunal Wadhwa

'''