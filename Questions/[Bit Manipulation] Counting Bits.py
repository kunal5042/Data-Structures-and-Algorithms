# Question: https://leetcode.com/problems/counting-bits/

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def countBits(self, n: int) -> List[int]:
        dp = [0 for _ in range(n+1)]
        offset = 1

        for num in range(1, n + 1):
            if offset * 2 == num:
                offset = num
            dp[num] = 1 + dp[num - offset]
            
        return dp
'''

# Kunal Wadhwa

'''