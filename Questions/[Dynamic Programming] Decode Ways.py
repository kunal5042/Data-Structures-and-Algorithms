# Question: https://leetcode.com/problems/decode-ways/

from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    
    def numDecodings(self, s: str) -> int:
        prev, cur = 1, 0 if s[0] == '0' else 1
        ways_previous = 1
        ways_current  = 0 if s[0] == '0' else 1
        
        for idx in range(1, len(s)):
            prev_of_ways_previous = ways_previous
            ways_previous = ways_current
            
            ways_current = 0
            
            if s[idx] != '0':
                # if say, all the ways we could decode the previous numbers
                # forms three strings
                # we know that current number will only map to one alphabet
                # if we add this alphabet to all those previous strings
                # we still have the same number of ways we can decode this new string
                # given that current number is not a 0
                
                ways_current = ways_previous
                
            if (s[idx-1] == '1') or (s[idx-1] == '2' and s[idx] not in '789'):
                # here, we realize that we can form a 2 digit number
                # if we take the previous digit and current digit
                # we know how many ways we can decode the string upto previous digit
                # and we know how many ways we can decode the string upto prev of previous digit
                # say we remove the previous digit from our string
                # now, the ways we can decode that string will be equal to prev_of_ways_previous
                # we take this previous digit and current digit to form a 2 digit number
                # in ways_current we already have stored the number of ways we can decode our string if we took current digit as only one digit number
                # now, we update it with number of ways we can decode if we took current and previous digit to form a 2 digit number
                # we do that, by adding prev_of_ways_previous to ways_current with reasoning that
                # if we add this 2 digit number to all the decoded strings of numbers upto 2 previous to current
                # we will have that many new decodings
                # and we add that to current
                ways_current += prev_of_ways_previous
                
        return ways_current	
'''

# Kunal Wadhwa

'''