# Question: https://leetcode.com/problems/swap-adjacent-in-lr-string/
# Medium


class Solution:
    # O(n) time and O(n) space
    def canTransform(self, start: str, end: str) -> bool:
        x = [char for char in start if char != 'X' ]
        y = [char for char in end   if char != 'X' ]
        
        if x != y: return False
        
        iter1 = iter2 = 0
        
        while iter1 < len(start) and iter2 < len(end):
            
            while iter1 < len(start) and start[iter1] == 'X':
                iter1 += 1
                
            while iter2 < len(end) and end[iter2] == 'X':
                iter2 += 1
                
            if iter1 == len(start) and iter2 == len(end):
                return True
                
            if iter1 == len(start) or iter2 == len(end):
                return False
            
            if start[iter1] == 'R' and iter1 > iter2:
                return False
            
            if start[iter1] == 'L' and iter2 > iter1:
                return False
            
            iter1 += 1
            iter2 += 1
            
        return True


# May 05, 2023

'''

# Kunal Wadhwa

'''