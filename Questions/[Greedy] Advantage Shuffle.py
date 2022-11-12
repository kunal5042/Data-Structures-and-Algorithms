# Question: https://leetcode.com/problems/advantage-shuffle/
# Medium

from typing import Optional, List
from collections import defaultdict

class Solution:
    # O(n*log(n)) Time and O(n) Space
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # saving the state of elements before sorting
        unsorted_indices = defaultdict(list)
        for idx, ele in enumerate(nums2):
            unsorted_indices[ele].append(idx)
            
        nums1.sort()
        nums2.sort()
        
        iter1 = iter2 = len(nums2)-1
        # pointer to smaller elements
        iter3 = 0
        
        # initializing space for result
        permutation = [None for _ in range(len(nums1))]
        
        while iter2 > -1:
            if nums1[iter1] > nums2[iter2]:
                # breakdown
                # iter2 = pointer to the element in nums2 which we are currently processing
                # nums2[iter2] = element we are currently processing
                # unsorted_indices[nums2[iter2]] = stack of indices \
                # at which current element is present in nums2 before sorting it
                # unsorted_indices[nums2[iter2]].pop() = get the top-most index from the stack
                permutation[unsorted_indices[nums2[iter2]].pop()] = nums1[iter1]
                iter1 -= 1
            else:
                # put the smallest element that's available
                permutation[unsorted_indices[nums2[iter2]].pop()] = nums1[iter3]
                iter3 += 1
            
            iter2 -= 1
        
        return permutation
    
            
    # O(n^2) Time and O(n) Space
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        options = Counter(nums1)
        best_permutation = []
        
        for idx in range(len(nums2)):
            closest_option = None
            
            # out of all elements that are available
            # among these all elements that are greater than current
            # pick the minimum of all these greater elements
            for ele in options:
                    
                if ele > nums2[idx]:
                    if closest_option is None:
                        closest_option = ele
                        continue
                        
                    closest_option = min(ele, closest_option)

            # if no greater element was found, replace with smallest element
            if closest_option is None: closest_option = min(options)
            best_permutation.append(closest_option)
            
            # decrement available count by 1
            options[closest_option] -= 1
            
            # if exhausted, remove from the hash
            if options[closest_option] == 0: del options[closest_option]
                
        return best_permutation
'''

# Kunal Wadhwa

'''