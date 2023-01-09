# Question: https://leetcode.com/problems/number-of-people-aware-of-a-secret/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(n) space
    def peopleAwareOfSecret(self, n, delay, forget):
        people_know = [0 for _ in range(n)]
        people_know[0] = 1
        can_share = 0
    
        mod = 10 ** 9 + 7
        
        for idx in range(1, n):
            can_share += people_know[idx - delay]
            can_share -= people_know[idx - forget]
            
            people_know[idx] = can_share
            
        return sum(people_know[~(forget-1):]) % mod


# January 09, 2023

'''

# Kunal Wadhwa

'''