# Question: https://leetcode.com/problems/remove-duplicate-letters/
# Medium

from collections import Counter

class Solution:
    # O(n) time and O(n) space
    def removeDuplicateLetters(self, s: str) -> str:
        # given s a string containing only lower case characters
        # s can have duplicate characters
        
        # len(s) >= 1
        
        # we need to remove duplicate letters 
        # we need to remove duplicates from s such that the resulting subsequence 
        # after removal is the smallest lexicographical order among all possible subsequences without duplicates
        
        # candidates for removal are any char whose freq > 1
        # we can make the best decision for each character
        
        # what makes a lexcio smallest sub sequence ?

        # what criteria do we need to remove a char?
        # will removal of this char lead to a lexcio smaller string?
        # if we want a smaller char to lead
        # we can only remove the chars before it, if there are duplicates present for them later in the string
        # in attempting for smaller chars to lead at every step, we can have the smallest lexcio possible subsequence
        
        in_stack = set()
        stack = []
        freq = Counter(s)
        
        for char in s:
            if char in in_stack:
                freq[char] -= 1
                continue
                
            while len(stack) != 0 and stack[~0] > char and freq[stack[~0]] >= 1:
                removed = stack.pop()
                in_stack.discard(removed)
                
            freq[char] -= 1
            stack.append(char)
            in_stack.add(char)
            
        return "".join(stack)
        


# September 26, 2023

'''

# Kunal Wadhwa

'''