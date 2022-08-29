# Question: https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# Medium
# To Do: O(1) Space
from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def repeatedNumber(self, A):
        missing_number   = None
        repeating_number = None
        array = [ele for ele in A]
        A = array
        
        for idx in range(len(A)):
            number = abs(A[idx])
            
            if A[number-1] < 0:
                repeating_number = number
            else:
                A[number-1] *= -1
                
        for idx in range(len(A)):
            if A[idx] > 0: missing_number = idx + 1
            
        return [repeating_number, missing_number]
        
'''

# Kunal Wadhwa

'''