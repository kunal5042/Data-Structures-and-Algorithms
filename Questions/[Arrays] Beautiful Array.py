# Question: https://leetcode.com/problems/beautiful-array/
# Medium
# Hard!
from typing import Optional, List

class Solution:
    # O(n*n) Time and O(n) Space
    def beautifulArray(self, n: int) -> List[int]:
        result = [1]
        
        while len(result) < n:
            updated = []
            
            for num in result:
                odd = (num * 2) -1
                if odd <= n: updated.append(odd)
                    
            for num in updated:
                even = (num * 2)
                if even <= n: updated.append(even)
                    
            result = updated
                    
        return result
'''

# Kunal Wadhwa

'''