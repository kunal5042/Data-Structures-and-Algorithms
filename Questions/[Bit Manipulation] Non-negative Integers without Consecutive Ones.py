# Question: https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
# Hard
from typing import Optional, List

class Solution:
    def findIntegers(self, n: int) -> int:
        fibo = [1, 2]
        for idx in range(2, 30):
            fibo.append(fibo[~0] + fibo[~1])
        
        result = one_before = 0
        
        for idx in reversed(range(30)):
            # check if the ith bit is set
            if (1 << idx) & n:
                result += fibo[idx]
                
                if one_before == 1:
                    result -= 1
                    break
                    
                one_before = 1
            else:
                one_before = 0
                
        return result + 1


# January 29, 2023

'''

# Kunal Wadhwa

'''