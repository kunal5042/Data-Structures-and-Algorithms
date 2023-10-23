# Question: https://leetcode.com/problems/h-index/
# Medium

from typing import List

class Solution:
    # O(n * log(n)) time and O(n) space
    def hIndex(self, citations: List[int]) -> int:
        # maximum value such that 
        # >= values are present in the array
            # which are >= this maximum value
            
        h_index = 0
        citations.sort()
        
        for idx, ele in enumerate(citations):
            number_of_papers = len(citations) - idx
            minimum_times_cited = ele
            if minimum_times_cited >= number_of_papers:
                h_index = max(h_index, number_of_papers)
            
        return h_index
        



# October 23, 2023

'''

# Kunal Wadhwa

'''