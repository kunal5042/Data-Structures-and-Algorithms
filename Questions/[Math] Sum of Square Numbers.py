# Question: https://leetcode.com/problems/sum-of-square-numbers/
# Medium

import math

class Solution:
    # O(n) time and O(n) space using two pointers
    def judgeSquareSum(self, c: int) -> bool:
        bar = math.floor(math.sqrt(c))
        array = [ele*ele for ele in range(0, bar+1)]
        
        start, end = 0, len(array)-1
        
        while start <= end:
            two_sum = array[start] + array[end]
            if two_sum == c:
                return True
            if two_sum < c:
                start += 1
            else:
                end -= 1
                
        return False
    
    # O(squareRoot(c) * log(c)) time and O(1) space
    def judgeSquareSum(self, c: int) -> bool:
        
        # logic if c - a^2 is a perfect square 
        # the equation can be true
        
        a = 0
        while a * a <= c:
            b = math.sqrt(c - a*a)
            if b == int(b):
                return True
            a += 1
        
        return False
    


# April 24, 2023

'''

# Kunal Wadhwa

'''