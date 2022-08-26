# Question: https://leetcode.com/problems/reverse-pairs/
# Hard
from typing import Optional, List

class Solution:
    # O(n * log(n)) + O(n) Time and O(n) Space 
    def reversePairs(self, nums: List[int]) -> int:
        def merge(left, middle, right):
            """Merges two sorted halves and counts the number of reverse pairs.
            Returns this count
            """
            pairs = 0
            idx, jdx = left, middle + 1
            
            # idx in [left, left + 1, . . , middle-1, middle]
            for idx in range(left, middle+1):
                while jdx <= right and nums[idx] > nums[jdx] * 2:
                    jdx += 1
                    
                # the count of elements which satisfied the condition
                pairs += (jdx - (middle + 1))
                
            temp = []
            # actual merge
            iter1, iter2 = left, middle + 1
            while iter1 <= middle and iter2 <= right:
                if nums[iter1] <= nums[iter2]:
                    temp.append(nums[iter1])
                    iter1 += 1
                else:
                    temp.append(nums[iter2])
                    iter2 += 1
                    
            # one array might have been exhausted before the other
            while iter2 <= right:
                temp.append(nums[iter2])
                iter2 += 1
                
            while iter1 <= middle:
                temp.append(nums[iter1])
                iter1 += 1
                
            # overwriting the original array
            for iter3 in reversed(range(left, right+1)):
                nums[iter3] = temp.pop()
            
            return pairs
        
        def merge_sort(low, high):
            """Sorts an array ranging from low to high inclusive. And computes the number
            of reverse pairs. Returns this pairs count
            """
            if low >= high: return 0
            middle = (low + high) // 2
            pairs  = merge_sort(low, middle)
            pairs += merge_sort(middle + 1, high)
            pairs += merge(low, middle, high)
            return pairs
        

        return merge_sort(0, len(nums)-1)
'''

# Kunal Wadhwa

'''