# Question: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Medium

from collections import defaultdict, Counter
from typing import List

class Solution:
    # O(len(s) * len(p)) time and O(len(p)) space
    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        anagram = defaultdict(int)
        required = Counter(p)
        
        start = None
        for end in range(len(s)):
            char = s[end]
            
            if char not in required:
                anagram = defaultdict(int)
                start = None
                continue
                
            anagram[char] += 1
            if start is None: start = end
                    
            if end - start + 1 == len(p):
                if anagram == required:
                    indices.append(start)
                    
                anagram[s[start]] -= 1
                if anagram[s[start]] == 0:
                    del anagram[s[start]]
                    
                start += 1
                
        return indices


# February 05, 2023

'''

# Kunal Wadhwa

'''