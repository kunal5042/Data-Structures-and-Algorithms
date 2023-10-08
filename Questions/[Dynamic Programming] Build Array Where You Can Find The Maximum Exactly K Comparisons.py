# Question: https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
# Hard

from functools import cache

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """
        An array such that 
        --> length of the array = n
        --> every element in array is gte 1 and lte m
        --> to find the maximum element using the linear search comparisons = k
        
        This function returns the number of ways to build a unique instance of array described above
        """
        
        # how to construct this array
        # we need k comparisons - k unique values in increasing order
        
        # n elements - data filing | changing order to create unique variations
        # m largest  - m needs be gte k | data filing using equal elements
        @cache
        def dp(i, max_so_far, remain):
            if i == n:
                if remain == 0:
                    return 1
                
                return 0
            
            ans = (max_so_far * dp(i + 1, max_so_far, remain)) % MOD
            for num in range(max_so_far + 1, m + 1):
                ans = (ans + dp(i + 1, num, remain - 1)) % MOD
                
            return ans
        
        MOD = 10 ** 9 + 7
        return dp(0, 0, k)
        


# October 08, 2023

'''

# Kunal Wadhwa

'''