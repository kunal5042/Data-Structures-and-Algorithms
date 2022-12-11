# Question: https://leetcode.com/problems/ones-and-zeroes/
# Medium
from typing import Optional, List

class Solution:
    # greedy approach: WA
    # example testcase
    # strs = ["111","1000","1000","1000"]
    # m = 9
    # n = 3
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        output = 0
        strs.sort(key=len)
        for bstring in strs:
            if m <= 0 and n <= 0: break
            counts = Counter(bstring)
            onecount = counts['1']
            zerocount = counts['0']
            if onecount <= n and zerocount <= m:
                output += 1
                n -= onecount
                m -= zerocount
        return output
    
    
    # this needs to be debugged
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        def decision_tree(length, zcount, ocount, idx):
            if zcount > m or ocount > n: return length-1
            if idx == len(strs): return length
            if (zcount, ocount, idx) in memo: return memo[(zcount, ocount, idx)]
            
            counts = Counter(strs[idx])
            include = decision_tree(length+1, zcount+counts['0'], ocount+counts['1'], idx+1)
            exclude = decision_tree(length, zcount, ocount, idx+1)
            memo[(zcount, ocount, idx)] = max(include, exclude)
            
            return memo[(zcount, ocount, idx)]
        
        decision_tree(0, 0, 0, 0)
        return memo[(0, 0, 0)]

    # logic and implementation is almost the same as above
    # instead of using a variable length, length is calculated by incrementing 1
    # O(2^n) Time and O(2^n) Space
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}
        def decision_tree(zcount, ocount, idx):
            if zcount > m or ocount > n: return -1
            if idx == len(strs): return 0
            if (zcount, ocount, idx) in memo: return memo[(zcount, ocount, idx)]
            
            counts = Counter(strs[idx])
            include = 1 + decision_tree(zcount+counts['0'], ocount+counts['1'], idx+1)
            exclude = decision_tree(zcount, ocount, idx+1)
            memo[(zcount, ocount, idx)] = max(include, exclude)
            
            return memo[(zcount, ocount, idx)]
        
        decision_tree(0, 0, 0)
        return memo[(0, 0, 0)]
'''

# Kunal Wadhwa

'''