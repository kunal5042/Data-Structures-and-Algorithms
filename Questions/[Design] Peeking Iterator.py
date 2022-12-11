# Question: https://leetcode.com/problems/peeking-iterator/
# Medium
from typing import Optional, List

# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.container = iterator
        self.last_call = 'initialize'
        self.cached = float('inf')

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.last_call == 'peek':
            return self.cached
        
        self.last_call = 'peek'
        self.cached = self.container.next()
        return self.cached
        
    def next(self):
        """
        :rtype: int
        """
        if self.last_call == 'peek':
            self.last_call = 'next'
            return self.cached
        
        self.cached = self.container.next()
        return self.cached
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.last_call == 'peek':
            return True
        
        return self.container.hasNext()
'''

# Kunal Wadhwa

'''