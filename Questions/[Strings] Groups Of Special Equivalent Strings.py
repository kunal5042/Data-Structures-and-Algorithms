# Question: https://leetcode.com/problems/groups-of-special-equivalent-strings/
# Medium
from typing import Optional, List


class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        def odd_even_map(string):
            _hash = {'odd': defaultdict(int), 'even': defaultdict(int)}
            for idx in range(len(string)):
                if idx % 2 == 0:
                    _hash['even'][string[idx]] += 1
                else:
                    _hash['odd'][string[idx]]  += 1
            return _hash
        
        unvisited = set(words)
        groups = 0
        
        while len(unvisited) != 0:
            add_back_cache = set()
            
            start = unvisited.pop()
            groups += 1
            group_signature = odd_even_map(start)
            
            while len(unvisited) != 0:
                candidate = unvisited.pop()
                candidate_signature = odd_even_map(candidate)
                if candidate_signature != group_signature:
                  add_back_cache.add(candidate)
                
            while len(add_back_cache) != 0:
                unvisited.add(add_back_cache.pop())
                
        return groups
    
    # O(max(words, key=len) * log(max(words, key=len))) Time and O(len(words)) Space
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        result = set()
        
        for word in words:
            signature = "".join(sorted(word[::2])) + "".join(sorted(word[::1]))
            result.add(signature)
            
        return len(result)
'''

# Kunal Wadhwa

'''