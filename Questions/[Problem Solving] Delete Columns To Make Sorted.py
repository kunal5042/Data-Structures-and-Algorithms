# Question: https://leetcode.com/problems/delete-columns-to-make-sorted/
# Easy
# 
from typing import Optional, List

from string import ascii_lowercase 
class Solution:
    # O(len(strs[0]) * len(strs)) Time and O(1) Space
    def minDeletionSize(self, strs: List[str]) -> int:
        _map = {}
        for idx, char in enumerate(ascii_lowercase):
            _map[char] = idx
            
        deletions = 0
        for col in range(len(strs[0])):
            buffer = _map[strs[0][col]]
            
            for idx in range(1, len(strs)):
                if buffer > _map[strs[idx][col]]:
                    deletions += 1
                    break
                
                buffer = _map[strs[idx][col]]
                
        return deletions
'''

# Kunal Wadhwa

'''