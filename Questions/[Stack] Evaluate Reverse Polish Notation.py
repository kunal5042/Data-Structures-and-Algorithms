# Question: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Medium
from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+' : lambda x, y: x + y,
            '-' : lambda x, y: y - x,
            '*' : lambda x, y: x * y,
            '/' : lambda x, y: int(y / x)
        }
        
        stack = []
        
        for token in tokens:
            if token in operators:
                stack.append(operators[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
                
        return stack[0]

    # O(n) time and O(n) space
    def evalRPN(self, tokens: List[str]) -> int:
        result = 0
        stack = []
        
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
                continue
                
            if len(stack) < 2: raise Exception('invalid')

            x = stack.pop()
            y = stack.pop()
            
            if token == '+': stack.append(y + x)
            if token == '-': stack.append(y - x)
            if token == '*': stack.append(y * x)
            if token == '/': stack.append(int(y / x))
                
        return stack.pop()
'''

# Kunal Wadhwa

'''