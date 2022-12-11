# Question: https://leetcode.com/problems/integer-to-roman/
# Medium
from typing import Optional, List

class Solution:
    def intToRoman(self, num: int) -> str:
        _hash = {
            1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
            6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
            40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
            900: 'CM', 1000: 'M'
        }
        
        result = ''
        
        for key in sorted(_hash.keys(), reverse=True):
            result += num // key * _hash[key]
            num %= key
            if num == 0: break
            
        return result


# November 19, 2022

'''

# Kunal Wadhwa

'''