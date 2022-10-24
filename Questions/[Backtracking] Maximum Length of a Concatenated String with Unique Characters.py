# Question: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# Medium
from typing import Optional, List

class Solution:
    # O(2^n) Time and O(n) Space
    def maxLength(self, arr: List[str]) -> int:
        max_len = [0]

        def helper(string, signature, idx):
            # updation at every level
            max_len[0] = max(len(string), max_len[0])

            # base-case
            if idx == len(arr):
                return

            # try all combinations
            for jdx in range(idx, len(arr)):
                cand_sign = set(arr[jdx])
                # if candidate is not feasible
                if len(cand_sign) != len(arr[jdx]):
                    continue
                    
                # if no common chars
                if len(signature.intersection(cand_sign)) == 0:
                    concat_str = string + arr[jdx]
                    concat_sign = set(concat_str)
                    helper(concat_str, concat_sign, jdx+1)

        helper('', set(), 0)
        return max_len[0]
'''

# Kunal Wadhwa

'''