# Question: https://leetcode.com/problems/find-the-difference/
# Easy

from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # t is a shuffling of s's characters + one more character
        # we have to return the one more character that was added to t
        
        # does s has duplicate characters? let's assume : yes
        
        # we can count the characters in s 
        # we can then loop through t and decrement the count of each char as and when visited in t
        # if we can't subtract any character or it is not found in s's counter
        # we immediately return that character
        
        char_freq_map = Counter(s)
        
        for char in t:
            if char not in char_freq_map or char_freq_map[char] == 0:
                return char
            char_freq_map[char] -= 1
            
        raise Exception("invalid input strings")


# September 25, 2023

'''

# Kunal Wadhwa

'''