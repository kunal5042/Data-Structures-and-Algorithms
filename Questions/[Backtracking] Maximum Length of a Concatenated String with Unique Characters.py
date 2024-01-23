# Question: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# Medium

from typing import List

class Solution:
    def __init__(self):
        self.max_len = 0
        self.arr = None
        
    def find_max_len(self, idx, rset):
        self.max_len = max(
            self.max_len,
            len(rset)
        )
        if idx == len(self.arr):
            return
        
        for jdx in range(idx, len(self.arr)):
            intersection = self.arr[jdx].intersection(rset)
            if len(intersection) == 0:
                self.find_max_len(jdx+1, self.arr[jdx].union(rset))
        
    def maxLength(self, arr: List[str]) -> int:
        valid_indices = []
        for idx, ele in enumerate(arr):
            arr[idx] = set(ele)
            if len(ele) == len(arr[idx]):
                valid_indices.append(idx)
                
        final_arr = []
        while len(valid_indices) != 0:
            final_arr.append(arr[valid_indices.pop()])
            
        self.arr = final_arr
        self.find_max_len(0, set())
        return self.max_len
            
        


# January 23, 2024

'''

# Kunal Wadhwa

'''