# Question: https://leetcode.com/problems/find-the-k-beauty-of-a-number/
# Easy
from typing import Optional, List

class Solution:
    # O(n^3) Time and O(1) Space
    def divisorSubstrings(self, num: int, k: int) -> int:
        # brute-force
        # generate all substrings
        # check if a substring meets the criteria, update the count
        
        snum  = str(num)
        count = 0
        
        for idx in range(len(snum)):
            substr = ''
            for jdx in range(idx, len(snum)):
                substr += snum[jdx]
                int_substr = int(substr)
                
                if int_substr == 0: continue
                    
                if len(substr) == k and num % int_substr == 0:
                    count += 1
                    
        return count
    
    # O(n) Time and O(1) Space
    def divisorSubstrings(self, num: int, k: int) -> int:
        snum  = str(num)
        count = 0
        
        # given k < len(str(nums))
        for idx in range(0, len(snum)-k+1):
            substr  = snum[idx:idx+k]
            int_sub = int(substr)
            if int_sub == 0: continue
            if num % int_sub == 0: count += 1
                
        return count
'''

# Kunal Wadhwa

'''