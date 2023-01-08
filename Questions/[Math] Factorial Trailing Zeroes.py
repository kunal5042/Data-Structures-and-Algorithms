# Question: https://leetcode.com/problems/factorial-trailing-zeroes/
# Medium
from typing import Optional, List

class Solution:
    factorial = {0:1, 1:1, 2:2}
    # O(n) time and O(n) space
    # bruteforce: accepted
    def trailingZeroes(self, n: int) -> int:
        def get_factorial(x):
            if x in Solution.factorial:
                return Solution.factorial[x]
            
            Solution.factorial[x] = x * get_factorial(x-1)
            return Solution.factorial[x]
        
        nfact = str(get_factorial(n))
        count = 0
        idx = len(nfact)-1
        while idx >= 0 and nfact[idx] == '0':
            count += 1
            idx -= 1
        return count
    
    # O(log_base_5(n)) time and O(1) space
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count


# January 08, 2023

'''

# Kunal Wadhwa

'''