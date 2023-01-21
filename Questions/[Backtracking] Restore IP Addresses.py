# Question: https://leetcode.com/problems/restore-ip-addresses/
# Medium
from typing import Optional, List

class Solution:
    # O(1) time and O(1) space
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        addresses = []
        
        def valid(part):
            if len(part) == 0 : return False
            if part[0] == '0' and len(part) > 1: return False
            if int(part) < 0  : return False
            if int(part) > 255: return False
            return True
        
        candidate = []
        def backtrack(part_no, start):
            if part_no == 4 and len(s) - 3 > start:
                return
            
            if part_no == 4:
                part = s[start:]
                if valid(part) is True:
                    candidate.append(part)
                    addresses.append('.'.join(candidate))
                    candidate.pop()
                    return
                
            for idx in range(start, start+3):
                part = s[start:idx+1]
                if valid(part) is True:
                    candidate.append(part)
                    backtrack(part_no+1, idx+1)
                    candidate.pop()
                    
        backtrack(1, 0)
        return addresses


# January 21, 2023

'''

# Kunal Wadhwa

'''