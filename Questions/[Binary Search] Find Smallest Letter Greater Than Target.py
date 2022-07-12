# Question: https://leetcode.com/problems/find-smallest-letter-greater-than-target/

from typing import Optional, List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        """ Takes a non-decreasing characters array and a target character
        Finds and returns the smallest character in the array that is larger
        than target. If no such character exists, then returns the smallest
        character from the array.
        """
        start, end = 0, len(letters) - 1
        result = None
        
        # window
        while start <= end:
            middle = (start + end) // 2
            
            if letters[middle] == target:
                start = middle + 1
                continue
            
            # update the result, and the window
            if letters[middle] > target:
                end    = middle - 1
                result = letters[middle]
            else:
                start = middle + 1
                
                
        # if no larger char found, return smallest char
        return result if result is not None else letters[0]
'''

# Kunal Wadhwa

'''