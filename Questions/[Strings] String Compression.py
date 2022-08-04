# Question: https://leetcode.com/problems/string-compression/

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    # Can easily be optimized to O(1) Space
    # By using a pointer for updation
    
    def compress(self, chars: List[str]) -> int:
        compressed = []
        
        def insert(buffer, count):
            if count > 1:
                compressed.append(buffer)
                for char in str(count):
                    compressed.append(char)

            else:
                compressed.append(buffer)
            
        # to keep track
        buffer, count = chars[0], 1
        
        for idx in range(1, len(chars)):
            if chars[idx] == buffer:
                count +=1 
                
            else:
                insert(buffer, count)
                buffer = chars[idx]
                count  = 1
                
        # uninserted char in buffer
        insert(buffer, count)

        # copy
        for idx in range(len(compressed)):
            chars[idx] = compressed[idx]
            
        return idx + 1
'''

# Kunal Wadhwa

'''