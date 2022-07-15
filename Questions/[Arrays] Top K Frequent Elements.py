# Question: https://leetcode.com/problems/top-k-frequent-elements/

from typing import Optional, List

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [ele for ele, freq in Counter(nums).most_common(k)]
'''

# Kunal Wadhwa

'''