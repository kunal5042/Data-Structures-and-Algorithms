# Question: https://leetcode.com/problems/remove-duplicate-letters*/

from typing import Optional, List

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        inserted, last_index = set(), {}
        stack = []
        
        for idx in reversed(range(len(s))):
            if s[idx] not in last_index: last_index[s[idx]] = idx
            
        for idx in range(len(s)):
            if s[idx] in inserted: continue

            while len(stack) != 0 and stack[~0] > s[idx]:
                # can we pop the top of stack?
                # if we can't find the char at stack top again
                # then we can't pop
                if idx > last_index[stack[~0]]: break
                
                # pop
                inserted.remove(stack[~0])
                stack.pop()
                
            stack.append(s[idx])
            inserted.add(s[idx])
        
        return ''.join(stack)
'''

# Kunal Wadhwa

'''