# Question: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# Medium


class Solution:
    # O(n) time and O(1) space 
    def maxVowels(self, s: str, k: int) -> int:
        result = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        for idx in range(k):
            result += 1 if s[idx] in vowels else 0
            
        start = 0
        current = result
        for end in range(k, len(s)):
            if s[start] in vowels:
                current -= 1
                
            if s[end] in vowels:
                current += 1
                
            result = max(result, current)
            start += 1
                        
        return result


# May 05, 2023

'''

# Kunal Wadhwa

'''