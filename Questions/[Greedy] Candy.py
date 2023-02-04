# Question: https://leetcode.com/problems/candy/
# Hard

from typing import List

class Solution:
    # O(n) time and O(n) space
    def candy(self, ratings: List[int]) -> int:
        # one candy to every child
        candies = [1 for _ in range(len(ratings))]
        
        for idx in range(0, len(ratings)):
            left = max(0, idx-1)
            
            if ratings[idx] > ratings[left]:
                candies[idx] = candies[left] + 1

        for idx in reversed(range(0, len(ratings))):
            right = min(len(ratings)-1, idx + 1)
            
            if ratings[idx] > ratings[right]:
                candies[idx] = max(candies[idx], candies[right] + 1)

        return sum(candies)
        



# February 04, 2023

'''

# Kunal Wadhwa

'''