# Question: https://leetcode.com/problems/closest-prime-numbers-in-range/
# Medium
from typing import Optional, List

class Solution:
    # O(n * log( log(n))) time and O(n) space 
    # where n is the upper-bound
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True for _ in range(right+1)]
        is_prime[0] = is_prime[1] = False
        
        # sieve
        for num in range(2, right+1):
            if num * num > right: break
            for non_prime in range(num*num, right+1, num):
                is_prime[non_prime] = False
        
        # filtering out
        primes = []
        for num in range(left, right+1):
            if is_prime[num] is True:
                primes.append(num)
              
        # finding pair
        if len(primes) < 2: return [-1, -1]
        pairs = [primes[0], primes[1]]
        for idx in range(2, len(primes)):
            if primes[idx] - primes[idx-1] < pairs[1] - pairs[0]:
                pairs = [primes[idx-1], primes[idx]]
                if pairs[1] - pairs[0] < 3: break
                
        return pairs



# January 20, 2023

'''

# Kunal Wadhwa

'''