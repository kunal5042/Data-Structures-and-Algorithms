# Question: https://leetcode.com/problems/top-k-frequent-words/
# Medium
from typing import Optional, List

from collections import Counter
class Solution:
    # O(n * log(n)) time and O(n) space
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [word for word, freq in Counter(sorted(words)).most_common(k)]


# November 19, 2022

'''

# Kunal Wadhwa

'''