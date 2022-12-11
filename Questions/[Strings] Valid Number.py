# Question: https://leetcode.com/problems/valid-number/
# Hard
# Just follow the valid number rules in order
from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def isNumber(self, s: str) -> bool:
        def one_or_more_digits(s):
            return len(s) > 0 and all([ch.isnumeric() for ch in s])
        
        def scrape_sign(s):
            return s[1:] if s[0] in "-+" else s
        
        def is_integer(s):
            if len(s) == 0: return False
            return one_or_more_digits(scrape_sign(s))
        
        def is_decimal(s):
            if len(s) == 0: return False
            parts = scrape_sign(s).split(".")
            if len(parts) != 2: return False
            a = parts[0]; b = parts[1]
            return (one_or_more_digits(a) and (len(b) == 0 or one_or_more_digits(b))) \
                    or (len(a) == 0 and one_or_more_digits(b))
        
        if 'e' in s or 'E' in s:
            parts = s.split('e') if 'e' in s else s.split('E')
            if len(parts) != 2: return False
            p1 = parts[0]; p2 = parts[1]
        else:
            p1 = s; p2 = "1"
        return (is_decimal(p1) or is_integer(p1)) and is_integer(p2)
'''

# Kunal Wadhwa

'''