# Question: https://leetcode.com/problems/remove-k-digits*/

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def removeKdigits(self, num: str, k: int) -> str:
        # using monotonic-stack and greedy approach
        
        # quick-escape
        if len(num) <= k: return "0"

        stack = []
        
        for char in num:
            # maintain monotonicity greedily
            while k > 0 and len(stack) != 0 and stack[~0] > char:
                k -= 1
                stack.pop()
                
            stack.append(char)
            
            
        # k not exhausted
        for _ in range(k): stack.pop()
        smallest_number = "".join(stack).lstrip("0")
        
        return smallest_number if len(smallest_number) != 0 else "0"
'''

# Kunal Wadhwa

'''