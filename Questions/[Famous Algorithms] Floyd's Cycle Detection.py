# Question: https://leetcode.com/problems/find-the-duplicate-number/

from typing import Optional, List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # PigeonHole Principle
        # Says that if we try to insert n items in m containers
        # and n > m, then at least two items will share the same container
        
        # Using Floyd's Cycle Detection Algorithm
        # 
        # because, there is at least and only one duplicate element
        # and all the elements are in range[1, n] inclusive
        # we can imagine the array as a linked list
        # where the duplicate elements points to the same node forming a cycle
        # 
        hare     = 0
        tortoise = 0
        
        while True:
            tortoise = nums[tortoise]
            hare     = nums[nums[hare]]
            
            if tortoise == hare:
                break
                
        # hare is already in the cycle
        # put the tortoise at the start of the list
        # and move both nodes one at a time
        # because the distance between the meeting point and the cycle's starting point
        # and the distance between the start of the list and the cycle's starting point is same
        # hare and tortoise will meet at the start of the cycle
        # and the start of our cycle is our duplicate element
        tortoise = 0
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare     = nums[hare]
                
        # return the duplicate element
        return tortoise

'''

# Kunal Wadhwa

'''