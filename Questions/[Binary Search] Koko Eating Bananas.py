# Question: https://leetcode.com/problems/koko-eating-bananas/

from typing import Optional, List

class Solution:
    # O(n * log(n)) Time and O(1) Space
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_eat_all(k: 'int') -> 'bool':
            """Returns true if koko can eat all bananas with an eating speed of k"""
            hours_required = 0
            for idx in range(len(piles)):
                hours_required += piles[idx] // k
                if piles[idx] % k != 0:
                    hours_required += 1
            
            return hours_required <= h
        
        low  = 1
        high = max(piles)
        
        min_k = None
        
        # binary-search
        while low <= high:
            middle = (low + high) // 2
            
            if can_eat_all(middle) is True:
                if min_k is None: min_k = middle
                    
                # update 
                min_k = min(min_k, middle)
                
                # try to minimize eating speed
                high = middle - 1
                
            else:
                # still haven't reached a valid eating speed
                # increase eating speed
                low = middle + 1
            
        return min_k
'''

# Kunal Wadhwa

'''