# Question: https://www.interviewbit.com/problems/subarray-with-given-xor/
# Medium
from typing import Optional, List

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # edge-case
        if len(A) == 0: return 0
        
        # base-case
        result = 1 if A[0] == B else 0
        
        # prefix_xor : frequency
        _hash = {A[0] : 1}
        
        prefix_xor = A[0]
        for idx in range(1, len(A)):
            prefix_xor ^= A[idx]
            
            if prefix_xor == B: result += 1
            
            if (prefix_xor ^ B) in _hash:
                result += _hash[prefix_xor ^ B]
            
            _hash[prefix_xor] = _hash.get(prefix_xor, 0) + 1
                
        return result
'''

# Kunal Wadhwa

'''