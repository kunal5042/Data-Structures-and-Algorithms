# Question: https://leetcode.com/problems/number-of-pairs-satisfying-inequality/
# Hard
from typing import Optional, List

from sortedcontainers import SortedList
from bisect import bisect_right
class Solution:
    # O(n * log(n)) time and O(n) space
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # we need
        # n1[i] - n1[j] <= n2[i] - n2[j] + diff
        
        # changing the equation we can get
        # n1[i] - n2[i] <= n1[j] - n2[j] + diff
        
        # we are going to store n1[i] - n2[i] in a sorted list 
        
        # then, for every every jth index
        # we are going to do a binary search on this sorted list
        # and find the index of (n1[j] - n2[j] + diff)
        
        # because the list is sorted, we add this index to our pairs
        # as all previous values are smaller than current and we can form
        # pair with each of them
        
        x = SortedList()
        pairs = 0
        
        for n1_j, n2_j in zip(nums1, nums2):
            pairs += x.bisect_right( n1_j - n2_j + diff)
            
            # n1_j and n2_j will act as n1_i and n2_i for next values
            x.add(n1_j - n2_j)
            
        return pairs



# January 02, 2023

'''

# Kunal Wadhwa

'''