# Question: https://leetcode.com/problems/perfect-squares/
# Medium
from typing import Optional, List

import math
class Solution:
    # every index stores the count of minimum number of perfect squares 
    # required to sum upto this index
    subproblem = [math.inf for idx in range((10**4)+1)]
    subproblem[0] = 0

    # O(n * n^(1/2)) Time and O(n) Space
    def numSquares(self, n: int) -> int:
        # static dp
        if Solution.subproblem[n] != math.inf: return Solution.subproblem[n]
        
        for idx in range(1, len(Solution.subproblem)):
            if Solution.subproblem[idx] == math.inf:
                start = idx
                break
                
        for num in range(start, n+1):
            # trying all the available perfect squares
            # to figure out the count of minimum perfect squares
            # and using the idea of coin-change problem to optimize this operation
            square_root = 1
            perfect_square = 1
            
            while perfect_square <= num:
                Solution.subproblem[num] = min(Solution.subproblem[num], 1+Solution.subproblem[num-perfect_square])
                square_root += 1
                perfect_square = square_root*square_root
                
        return Solution.subproblem[n]
'''

# Kunal Wadhwa

'''