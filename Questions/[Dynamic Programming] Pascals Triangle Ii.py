# Question: https://leetcode.com/problems/pascals-triangle-ii/
# Easy
from typing import Optional, List


class Solution:
    # O(n) Time and O(n) Space
    def getRow(self, row_index: int) -> List[int]:
        if row_index == 0: return [1]
        
        dp = [1]
        
        for row in range(1, row_index+1):
            new_row = [None] * (len(dp)+1)
            
            for idx in range(len(new_row)):
                ele = 0
                if len(dp) > idx - 1 >= 0  : ele += dp[idx-1]
                if idx < len(dp): ele += dp[idx]
                new_row[idx] = ele
                
            dp = new_row
            
        return dp
'''

# Kunal Wadhwa

'''