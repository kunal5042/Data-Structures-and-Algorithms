# Question: https://www.codingninjas.com/codestudio/problems/sort-a-stack_985275?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0
# Easy
from typing import Optional, List

from collections import deque
def monotonous_insert(stack, val):
    if len(stack) == 0 or stack[~0] <= val:
        stack.append(val)
        return
    
    popped = stack.pop()
    monotonous_insert(stack, val)
    stack.append(popped)
        
def sortStack(stack):
    if len(stack) == 0:
        return
    
    popped = stack.pop()
    sortStack(stack)
    monotonous_insert(stack, popped)
    return stack
    
    
'''

# Kunal Wadhwa

'''