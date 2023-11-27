# Question: https://leetcode.com/problems/the-kth-factor-of-n/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency
# The Kth Factor Of N

import math

class Solution:
    # O(n) time and O(n) space
    def kthFactor(self, n: int, k: int) -> int:
        if k == 1: return 1
        factors = [1]
        for idx in range(2, n+1):
            if n % idx == 0:
                factors.append(idx)
            
            if len(factors) == k:
                return factors[~0]

        return -1

    # O(root(n)) time and O(root(n)) space
    def kthFactor(self, n: int, k: int) -> int:
        delta = []
        gamma = []

        for idx in range(1, int(math.sqrt(n))+1):
            if n % idx == 0:
                delta.append(idx)
                gamma.append(n // idx)

        if delta[~0] == gamma[~0]:
            gamma.pop()

        factors = delta + gamma[::-1]
        return -1 if len(factors) < k else factors[k-1]


# November 27, 2023

'''

# Kunal Wadhwa

'''