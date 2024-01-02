# Question: https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/description/
# Medium

from collections import Counter
from typing import List

class Solution:
    # O(n*n) time and O(n) space
    def findMatrixNaive(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        row_count = max(counts.values())
        matrix = [[] for _ in range(row_count)]

        row_no = 0
        while len(counts) != 0:
            delete_keys = []
            for ele, freq in counts.items():
                if freq > 1:
                    counts[ele] -= 1
                else:
                    delete_keys.append(ele)

                matrix[row_no].append(ele)

            for key in delete_keys:
                del counts[key]

            row_no += 1

        return matrix

    # O(n) time and O(n) space
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        matrix = [[]]
        counts = {}

        for ele in nums:
            counts[ele] = counts.get(ele, 0) + 1
            if counts[ele] > len(matrix):
                matrix.append([])

            matrix[counts[ele]-1].append(ele)

        return matrix


# January 02, 2024

'''

# Kunal Wadhwa

'''