# Question: https://leetcode.com/problems/minimum-suffix-flips/
# Medium
from typing import Optional, List

class Solution:
    def minFlips(self, target: str) -> int:
        # s = '00000' where len(target) == len(s) always holds True
        # you want to make s == target
        # you can do that using one type of an operation
        # this operation can be performed any number of times
        
        # in one instance of this operation
        # you can pick any value of i from range 0 <= i <= n-1
        # and flip all bits in the range starting from i upto and including n-1
        
        # the goal is to return the minimum number of operations 
        # required to convert s into target
        
        # target = 101, s = 000
        # s = 111
        # s = 100
        # s = 101
        # operations = 3
        
        # target = 10111, s = 00000
        # s = 00111
        # s = 11000
        # s = 10111
        # operations = 3
        
        # thought-process for brute-force
        # the idea is to start with matching the first k ones to the target
        # such that all ones are consecutive
        # for example
        
        # if target = 110011, s = 000000
        # first operation = 111111
        
        # if target = 001100, s = 000000
        # first operation = 001111
        
        # if target = 101010, s = 000000
        # first operation = 111111
        
        # continuing on, keep matching the next consecutive ones or zeroes
        # which are unmatched to the target
        # skip any ones or zeroes which are in correct position
        # moving ahead in previous three examples respectively
        
        # second operation = 110000
        # third operation  = 110011
        
        # second operation = 001100
        
        # second operation = 100000
        # third operation  = 101111
        # fourth operation = 101000
        # fifth operation  = 101011
        # sixth operation  = 101010
        
        # algorithm
        # start with finding the first consecutive ones or zeroes
        # such that they are unmatched when compared 
        # flip all bits starting from the first position of these unmatched
        # consecutive ones or zeroes
        # perform the above 3 steps as long as s != target
        # keep track of the number of operations performed
        
        # brute-force code
        # O(n*n) time and O(1) space
        
        def flip(string):
            result = []
            for char in string:
                if char == '0': result.append('1')
                if char == '1': result.append('0')
            return ''.join(result)
        
        s = ''.join(['0' for _ in range(len(target))])
        operations = 0
        idx = 0
        while s != target:
            while idx < len(s) and s[idx] == target[idx]:
                idx += 1
                
            if idx == len(target): break
                
            substring_length = 0
            buffer = s[idx]
            jdx = idx
            while jdx < len(s) and s[jdx] == buffer:
                substring_length += 1
                jdx += 1
            
            s = s[:idx] + flip(s[idx:])
            operations += 1
            
        return operations
    
    def minFlips(self, target: str) -> int:
        # thought process for optimization
        # whenever we find a non matching one or a zero
        # we flip it, including all the remaining ones after it
        # in the right direction
        # hence we can maintain a state of remaining chars in the s
        # and whenever corresponding char in target doesn't match state
        # we perform flips on this char and remaining right half
        # and instead of actually doing the flip we flip our state
        # we keep track of total flips of the state
        
        # O(n) time and O(1) space
        state = '0'
        operations = 0
        for digit in target:
            if digit == state:
                continue
            state = '0' if state != '0' else '1'
            operations += 1
        
        return operations
                
                


# December 25, 2022

'''

# Kunal Wadhwa

'''