# Question: https://practice.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
# Medium
from typing import Optional, List

class Solution:
    # O(n) Time and O(k) Space
    def longestKSubstr(self, s, k):
        # code here
        if k == 0 or k > len(s) or len(s) == 0:
            return -1
            
        result = -1
        start  = 0
        window = {s[start] : 1}
        
        for idx in range(1, len(s)):
            window[s[idx]] = window.get(s[idx], 0) + 1
            
            while len(window) > k:
                window[s[start]] -= 1
                if window[s[start]] == 0:
                    del window[s[start]]
                    
                start += 1
                
            if len(window) == k:
                result = max(result, idx - start + 1)
            
            
        return result
'''

# Kunal Wadhwa

'''