# Question: https://leetcode.com/problems/reverse-vowels-of-a-string/
# Easy
from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left, right = 0, len(s)-1
        output = [char for char in s]
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                output[left] = s[right]
                output[right] = s[left]
                left += 1
                right -= 1
                
            elif s[left] in vowels:
                right -= 1
                
            elif s[right] in vowels:
                left += 1
            
            else:
                left += 1
                right -= 1
                
        return "".join(output)
'''

# Kunal Wadhwa

'''