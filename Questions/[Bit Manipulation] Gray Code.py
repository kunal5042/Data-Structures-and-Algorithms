# Question: https://leetcode.com/problems/gray-code/
# Medium
from typing import Optional, List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if not n: return [0]
        result = [0, 1]
        for idx in range(2, n+1):
            for jdx in range(len(result)-1, -1, -1):
                result.append(result[jdx] | 1 << idx - 1)
                
        return result


# December 29, 2022

'''

# Kunal Wadhwa

'''