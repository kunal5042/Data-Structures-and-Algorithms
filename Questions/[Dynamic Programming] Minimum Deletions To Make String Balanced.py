# Question: https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/
# Medium

from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    
    def minimumDeletions(self, s: str) -> int:
        deletions = 0
        b_count   = 0
        
        for char in s:
            if char == "a":
                # either delete all b upto this point
                # or delete this 'a'
                deletions = min(b_count, deletions + 1)
            else:
                b_count += 1
        
        return deletions
'''

# Kunal Wadhwa

'''