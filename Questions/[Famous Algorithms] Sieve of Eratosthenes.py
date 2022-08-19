# Question: https://leetcode.com/problems/count-primes/submissions/
# Medium
from typing import Optional, List

class Solution:
    def countPrimes(self, n: int) -> int:
        # quick escape
        if n < 3: return 0
        
        primes = [True for _ in range(n)]
        # base-case
        primes[0] = primes[1] = False
        
        non_prime_count = 2

        # filter out non-primes
        for num in range(2, n):
            if num*num >= n: break
            if primes[2] is False: continue
                
            for jdx in range(num*num, n, num):
                if primes[jdx] is True : non_prime_count += 1
                primes[jdx] = False

                
        return len(primes) - non_prime_count
'''

# Kunal Wadhwa

'''