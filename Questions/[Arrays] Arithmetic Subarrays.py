# Question: https://leetcode.com/problems/arithmetic-subarrays/description/
# Medium

from typing import List

class Solution:
    def isAirthmetic(self, array):
        if len(array) < 2: return False
        delta = array[1] - array[0]
        for idx in range(2, len(array)):
            if array[idx] - array[idx-1] != delta:
                return False
        return True

    def checkArithmeticSubarraysNaive(self, nums: List[int], lbound: List[int], rbound: List[int]) -> List[bool]:
        result = []

        for idx in range(len(lbound)):
            left = lbound[idx]
            right = rbound[idx]
            subarray = sorted(nums[left:right+1])
            result.append(self.isAirthmetic(subarray))

        return result

    def checkArithmeticSubarrays(self, nums: List[int], lbound: List[int], rbound: List[int]) -> List[bool]:
        result = []

        for idx in range(len(lbound)):
            left = lbound[idx]
            right = rbound[idx]
            subarray = (nums[left:right+1])
            sub_set = set(subarray)
            sub_max = max(subarray)
            sub_min = min(subarray)
            if (sub_max - sub_min) % (len(subarray) - 1) != 0:
                result.append(False)
                continue
            
            sub_diff = (sub_max - sub_min) // (len(subarray) - 1)
            cur = sub_min
            flag = True
            while cur != sub_max:
                cur += sub_diff
                if cur not in sub_set:
                    flag = False
                    break
            result.append(flag)
 
        return result


# November 23, 2023

'''

# Kunal Wadhwa

'''