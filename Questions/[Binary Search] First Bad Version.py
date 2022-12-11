# Question: https://leetcode.com/problems/first-bad-version/
# Easy
from typing import Optional, List

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    # O(log(n)) Time and O(1) Space
    def firstBadVersion(self, n: int) -> int:
        """Takes an integer n.
        Provided a helper function that returns a boolean
        Finds and returns the first integer in the range 1-n for which
        helper returns True
        """
        
        left, right = 1, n
        result = None
        
        while left <= right:
            middle = (left + right) // 2
            
            if isBadVersion(middle) is True:
                result = middle
                right  = middle -1
                continue
                
            left = middle + 1
            
        return result
'''

# Kunal Wadhwa

'''