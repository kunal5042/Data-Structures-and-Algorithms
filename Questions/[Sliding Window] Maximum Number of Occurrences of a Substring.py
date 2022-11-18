# Question: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/
# Medium
from typing import Optional, List

class Solution:
    # O(n*k) time and O(n*k) space
    def maxFreq(self, s: str, max_letters: int, min_size: int, max_size: int) -> int:
        subs = defaultdict(int)
        for idx in range(len(s)):
            substring_list = []
            for jdx in range(idx, idx + min_size):
                if jdx == len(s):
                    substring_list.clear()
                    break
                substring_list.append(s[jdx])
                
            substring = "".join(substring_list)
            
            if len(set(substring)) <= max_letters and substring != '':
                subs[substring] += 1
            
        if len(subs) == 0: return 0
        return max(subs.values())
'''

# Kunal Wadhwa

'''