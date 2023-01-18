# Question: https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
# Medium
from typing import Optional, List

class Solution:
    # brute-force: TLE 177/201
    # O(2^k) time and O(2^k) space
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s): return False
        
        bcode = set()
        def binary_codes(coding):
            if len(coding) == k:
                bcode.add("".join(coding))
                return 
            
            for digit in ['0', '1']:
                coding.append(digit)
                binary_codes(coding)
                coding.pop()
                
            return
        
        binary_codes([])
        
        window_start = 0
        for window_end in range(len(s)):
            if window_end - window_start + 1 == k:
                bstring = s[window_start:window_end+1]
                if bstring in bcode:
                    bcode.remove(bstring)
                window_start += 1
        
        return len(bcode) == 0
    
    # O(n*k) time and O(n*k) space
    def hasAllCodes(self, s: str, k: int) -> bool:
        bcode = set()
        total_bcodes = 2**k
        window_start = 0
        for window_end in range(len(s)):
            if window_end - window_start + 1 == k:
                bstring = s[window_start:window_end+1]
                if bstring not in bcode:
                    bcode.add(bstring)
                    total_bcodes -= 1
                window_start += 1
        
        return total_bcodes == 0        


# January 18, 2023

'''

# Kunal Wadhwa

'''