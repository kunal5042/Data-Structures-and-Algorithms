# Question: https://leetcode.com/problems/longest-substring-without-repeating-characters/

from typing import Optional, List

class Solution:
    '''
    O(n) Time and O(n) Space: where n is the length of the input string
    '''
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        result  = 0
        # keeping track of visited elements/ repeating elements
        visited = {}
        
        # marks the start of the current substring with all non repeating characters
        substring_start = 0
        
        for current_idx, char in enumerate(s):
            # if the current character is repeated before but also
            # only if it's repeated index is greater than the current substring with all non repeating character's start
            # that is, it's relevant to our current substring
            # only then it will be a problem and we will have to discard our current substring
            # and update it with new substring which doesn't include the repeating character
            # that is, we remove it from the left by incrementing the start of previous substring
            
            if char in visited and visited[char] >= substring_start:
                substring_start = visited[char] + 1
            
            
            # keep updating the result, as we keep calculating current substring without any repeating characters
            result = max(result, current_idx - substring_start + 1)
            
            # and mark the current character visited as we go
            visited[char] = current_idx
            
        return result
'''

# Kunal Wadhwa

# GitHub     : https://github.com/kunal5042
# LeetCode   : https://leetcode.com/kunal5042/
# HackerRank : https://www.hackerrank.com/kunalwadhwa_cs
# LinkedIn   : https://www.linkedin.com/in/kunal5042/

'''