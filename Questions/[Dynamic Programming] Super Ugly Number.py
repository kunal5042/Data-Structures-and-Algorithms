# Question: https://leetcode.com/problems/super-ugly-number/

from typing import Optional, List

class Solution:
    def nthSuperUglyNumber_BRUTE_FORCE(self, n: int, primes: List[int]) -> int:
        def is_super_ugly(number) -> bool:
            """
            Checks if the given number is super ugly
            Args:
                number: int
                
            Returns: bool
            """
            for prime in primes:
                while number % prime == 0:
                    number = number // prime
            return number == 1
        
        count = 1
        number = 1
        # for every number check if it's super ugly
        # increment count accordingly
        # when count == nth
        # return the number
        while True:
            if count == n: return number
            number += 1
            if is_super_ugly(number): count += 1
        
        return
    
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        def get_next_ugly(pointer_map) -> int:
            """
            Has a reference to dp array and takes in a hashmap, returns
            the next ugly number.
            
            Args:
                pointer_map: dict(prime, pointer) where pointer points to the index in dp array
                
            Returns:
                Next ugly number as an integer.
                result: int 
            """
            result = float('inf')
            prime_used = None
            for prime, pointer in pointer_map.items():
                # increment the pointer as we don't want duplicates
                if prime * dp[pointer] == result:
                    pointer_map[prime] += 1
                    
                if prime * dp[pointer] < result:
                    result = prime * dp[pointer]
                    prime_used = prime

            # increment the pointer of the prime number we used 
            # for this ugly number
            pointer_map[prime_used] += 1
            return result
            
        # initialize 
        dp = [1 for _ in range(n)]
        pointer_map = { key:0 for key in primes }
        
        for idx in range(1, len(dp)):
            dp[idx] = get_next_ugly(pointer_map)
        
        return dp[~0]
'''

# Kunal Wadhwa

'''