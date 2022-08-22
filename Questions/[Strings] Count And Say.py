# Question: https://leetcode.com/problems/count-and-say/
# Medium
from typing import Optional, List

class Solution:
    # O(n * max(said, key=len)) Time and O(n) Space
    def countAndSay(self, n: int) -> str:
        def say(string):
            if len(string) == 0: return ''
            result = ''
            buffer = string[0]
            count  = 1
            
            idx = 1
            while idx < len(string):
                if string[idx] == buffer:
                    count += 1
                else:
                    result += str(count) + buffer
                    buffer = string[idx]
                    count  = 1
                    
                idx += 1
            
            return result + str(count) + buffer
        
        
        said = ['' for _ in range(n)]
        said[0] = '1'
        
        for idx in range(1, n):
            said[idx] = say(said[idx-1])
            
        return said[~0]
    
'''

# Kunal Wadhwa

'''