# Question: https://leetcode.com/problems/valid-parentheses/

from typing import Optional, List

class Solution:
    def isValid(self, s: str) -> bool:
        
        def match(open_bracket, close_bracket):
            x, y = open_bracket, close_bracket
            
            if x == '(' and y == ')': return True
            if x == '[' and y == ']': return True
            if x == '{' and y == '}': return True
            
            return False
        
        def is_an_open(bracket):
            if bracket == '(' or \
            bracket == '[' or \
            bracket == '{':
                return True
            return False
        
        # initializing empty stack for storing open brackets
        stack = []
        
        # given that string consists of only brackets
        for bracket in s:
            
            if is_an_open(bracket):
                stack.append(bracket)
                
            else:
                # no open bracket in stack to match with equals invalid
                if len(stack) == 0:
                    return False

                # closing bracket 
                # match it with corresponding open bracket in the stack
                if match(stack.pop(), bracket) is False:
                    return False
                
                
        # if all open and closing brackets were matched
        # and there is no umatched bracket left
        if len(stack) == 0: return True
        
        # if unmatched bracket is left
        return False

'''

# Kunal Wadhwa


'''