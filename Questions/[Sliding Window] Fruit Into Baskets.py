# Question: https://leetcode.com/problems/fruit-into-baskets/
# Medium
from typing import Optional, List

class Solution:
    # O(n) time and O(1) space
    def totalFruit(self, fruits: List[int]) -> int:
        maxfruits = 1
        baskets = set([fruits[0]])
        window_start = 0
        occurence = {fruits[0]:0}
        
        for window_end in range(1, len(fruits)):
            if len(baskets) < 2 or fruits[window_end] in baskets:
                baskets.add(fruits[window_end])
                
            else:
                to_discard = None
                last_appeared = float('inf')

                # find the optimal choice of removal
                for fruit in baskets:
                    if occurence[fruit] < last_appeared:
                        last_appeared = occurence[fruit]
                        to_discard = fruit

                # remove and add the new type of fruit
                baskets.remove(to_discard)
                baskets.add(fruits[window_end])
                window_start = occurence[to_discard] + 1
            
            # update
            occurence[fruits[window_end]] = window_end
            maxfruits = max(maxfruits, window_end - window_start + 1)
            
        return maxfruits


# January 28, 2023

'''

# Kunal Wadhwa

'''