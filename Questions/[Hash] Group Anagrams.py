# Question: https://leetcode.com/problems/group-anagrams/

from typing import Optional, List

from collections import defaultdict
class Solution:
    # O(n * m(log(m))): where n is the length of the input list and m is the length
    # of the longest word
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Takes a list of strings.
        Groups all the anagrams into a new list for each group
        Returns all of these groups in a new list
        """
        
        _hash = defaultdict(list)
        
        for string in strs:
            anag = "".join(sorted(string))
            _hash[anag].append(string)
            
        return list(_hash.values())
'''

# Kunal Wadhwa

'''