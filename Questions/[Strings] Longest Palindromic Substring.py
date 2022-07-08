# Question: https://leetcode.com/problems/longest-palindromic-substring/

from typing import Optional, List

class Solution:
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s
        
        max_palindrome_len   = 0
        max_palindrome_start = 0
        max_palindrome_end   = 0
        
        for idx in range(0, len(s)):

            # odd palindrome
            current_palindrome_len = 1
            left = idx - 1
            right = idx + 1
            
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    current_palindrome_len += 2
                    left  -= 1
                    right += 1
                else:
                    break
            
            if current_palindrome_len > max_palindrome_len:
                max_palindrome_len = current_palindrome_len
                max_palindrome_start = left+1
                max_palindrome_end   = right
                
        
            # even palindrome
            current_palindrome_len = 0
            left  = idx - 1
            right = idx
            
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    current_palindrome_len += 2
                    left  -= 1
                    right += 1
                else:
                    break
            
            if current_palindrome_len > max_palindrome_len:
                max_palindrome_len = current_palindrome_len
                max_palindrome_start = left+1
                max_palindrome_end   = right
                
                
        return s[max_palindrome_start:max_palindrome_end]
'''

# Kunal Wadhwa


'''