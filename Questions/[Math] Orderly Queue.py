# Question: https://leetcode.com/problems/orderly-queue/
# Hard
from typing import Optional, List

class Solution:
    # O(n*n) Time and O(n) Space
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            return min(s[idx:] + s[:idx] for idx in range(len(s)))
        else:
            return ''.join(sorted(s))
'''

# Kunal Wadhwa

'''