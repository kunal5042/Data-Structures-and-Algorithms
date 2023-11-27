# Question: https://leetcode.com/problems/wildcard-matching/description/
# Wildcard Matching

from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # ? - matches a single character
        # * - matches any sequence including empty string
        if len(s) == 0:
            for ele in p:
                if ele != '*':
                    return False
            return True

        @cache
        def can_match(idx, jdx):
            if idx == len(s):
                if jdx == len(p):
                    return True

                for ele in p[jdx:]:
                    if ele != '*':
                        return False

                return True
            
            if jdx >= len(p):
                return False

            if idx >= len(s):
                return False

            ele = p[jdx]
            if ele == s[idx]:
                return can_match(idx+1, jdx+1)

            if ele == '?':
                return can_match(idx+1, jdx+1)

            if ele == '*':
                if can_match(idx+1, jdx+1) is True:
                    return True

                if can_match(idx, jdx+1) is True:
                    return True

                if can_match(idx+1, jdx) is True:
                    return True
                    
            return False

        return can_match(0, 0)


# November 27, 2023

'''

# Kunal Wadhwa

'''