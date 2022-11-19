# Question: from collections import Counter
#     # O(N * Log(N)) Time And O(N) Space
from typing import Optional, List

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [word for word, freq in Counter(sorted(words)).most_common(k)]


# November 19, 2022

'''

# Kunal Wadhwa

'''