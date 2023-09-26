# Question: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# Medium

from collections import Counter

class Solution:
    # O(n) time and O(n) s[space]
    def smallestSubsequence(self, string: str) -> str:
        freq = Counter(string)
        visited = set()
        stack = []
        
        for char in string:
            if char in visited:
                freq[char] -= 1
                continue
                
            while len(stack) != 0 and stack[~0] > char and freq[stack[~0]] >=1:
                visited.discard(stack.pop())
                
            visited.add(char)
            freq[char] -= 1
            stack.append(char)
            
        return "".join(stack)


# September 26, 2023

'''

# Kunal Wadhwa

'''