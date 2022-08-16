# Question: https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

from typing import Optional, List

from string import ascii_lowercase as alphabets
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alpha_map = {char: idx+1 for idx, char in enumerate(alphabets)}
        converted = ''
        for char in s: converted += str(alpha_map[char])

            
        for _ in range(k):
            _sum = 0
            for char in converted: _sum += int(char)
            converted = str(_sum)
            
        return int(converted)
'''

# Kunal Wadhwa

'''