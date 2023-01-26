# Question: https://leetcode.com/problems/distinct-echo-substrings/
# Hard
from typing import Optional, List

class Solution:
    # O(n * n) time and O(n * n) space
    def distinctEchoSubstrings(self, text: str) -> int:
        echo_substrings = set()
        
        for length in range(1, (len(text)//2)+1):
            left = 0
            right = length
            count = 0
            
            while right < len(text):
                if text[left] == text[right]:
                    count += 1
                else:
                    count = 0
                    
                if count == length:
                    echo_substrings.add(text[left-length+1:right+1])
                    count -= 1
                
                left += 1
                right += 1
            
        return len(echo_substrings)



# January 26, 2023

'''

# Kunal Wadhwa

'''