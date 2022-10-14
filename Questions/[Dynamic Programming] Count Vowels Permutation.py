# Question: https://leetcode.com/problems/count-vowels-permutation/
# Hard
from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def countVowelPermutation(self, n: int) -> int:
        # where row is in range [1,5] and {1:a, 2:e, 3:i, 4:o, 5:u}
        # and col corresponds to the length of the string
        # dp[row][col] stores the number of strings of length col that can be formed with ending char equal to row 
        dp = [[0 for _ in range(n+1)] for _ in range(6)]
        for row in range(1, 5+1): dp[row][1] = 1

        a, e, i, o, u = 1, 2, 3, 4, 5
        mod = (10**9) + 7
        res = 0
        
        for string_length in range(2, n+1):
            col = string_length
            # a string can end with a
            # only if previous char was either of [e, u, i]
            # hence, the count of strings the can end with a equals to
            dp[a][col] = (dp[e][col-1] + dp[u][col-1] + dp[i][col-1]) % mod
            
            # similarly
            dp[e][col] = (dp[a][col-1] + dp[i][col-1]) % mod
            dp[i][col] = (dp[o][col-1] + dp[e][col-1]) % mod
            dp[o][col] = (dp[i][col-1]) % mod
            dp[u][col] = (dp[i][col-1] + dp[o][col-1]) % mod
            
        # compute total
        for row in range(1, 5+1):
            col = len(dp[0])-1
            res += dp[row][col]
            res %= mod
        return res
    
    # O(n) Time and O(1) Space
    def countVowelPermutation(self, n: int) -> int:
        pa, pe, pi, po, pu = 1, 1, 1, 1, 1
        a, e, i, o, u = 1, 2, 3, 4, 5
        mod = (10**9) + 7
        res = 0
        
        for string_length in range(2, n+1):
            a = pe + pu + pi
            e = pa + pi
            i = pe + po
            o = pi
            u = pi + po
            
            pa, pe, pi, po, pu = a, e, i, o, u
            
        # compute total
        return (pa + pe + pi + po + pu) % mod
'''

# Kunal Wadhwa

'''