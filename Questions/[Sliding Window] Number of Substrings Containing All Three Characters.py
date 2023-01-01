# Question: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(1) space
    def numberOfSubstrings(self, s: str) -> int:
        def at_least_one_occurence(hash_map):
            for val in hash_map.values():
                if val == 0:
                    return False
            return True
        
        substrings = 0
        window_start = 0
        occurences = {char:0 for char in 'abc'}
        
        for window_end in range(len(s)):
            occurences[s[window_end]] = occurences.get(s[window_end], 0) + 1
            
            while len(occurences) == 3 and at_least_one_occurence(occurences):
                occurences[s[window_start]] -= 1
                if occurences[s[window_start]] == 0:
                    del occurences[s[window_start]]
                    
                window_start += 1
            
            substrings += window_start
                
        return substrings


# January 01, 2023

'''

# Kunal Wadhwa

'''