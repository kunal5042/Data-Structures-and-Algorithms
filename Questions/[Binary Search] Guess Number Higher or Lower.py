# Question: https://leetcode.com/problems/guess-number-higher-or-lower/
# Easy
from typing import Optional, List

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    # O(log(n)) time and O(1) space
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while left <= right:
            middle = (left + right) // 2
            
            result = guess(middle)
            if result == 0:
                return middle
            
            if result == -1:
                right = middle - 1
            else:
                left = middle + 1
                
        raise Exception("Couldn't guess the number!")
'''

# Kunal Wadhwa

'''