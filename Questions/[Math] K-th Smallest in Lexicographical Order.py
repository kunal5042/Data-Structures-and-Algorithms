# Question: https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# Hard
from typing import Optional, List

class Solution:
    # O(log(n)^2) time and O(1) space
    # inspired by zhiqing_xiao's solution
    def findKthNumber(self, n: int, k: int) -> int:
        result = 1;
        k -= 1
        while k > 0:
            count = 0
            interval = [result, result+1]
            while interval[0] <= n:
                count += (min(n+1, interval[1]) - interval[0])
                interval = [10*interval[0], 10*interval[1]]

            if k >= count:
                result += 1
                k -= count
            else:
                result *= 10
                k -= 1
        return result


# January 29, 2023

'''

# Kunal Wadhwa

'''