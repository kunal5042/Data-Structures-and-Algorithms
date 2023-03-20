# Question: https://leetcode.com/problems/can-place-flowers/
# Easy

from typing import List

class Solution:
    # O(n) time and O(1) space
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for idx in range(len(flowerbed)):
            
            # Check if the current plot is empty.
            if flowerbed[idx] == 0:
                
                # Check if the left and right plots are empty.
                empty_left_plot = (idx == 0) or (flowerbed[idx - 1] == 0)
                empty_right_lot = (idx == len(flowerbed) - 1) or (flowerbed[idx + 1] == 0)
                
                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[idx] = 1
                    count += 1
                    if count >= n:
                        return True
                    
        return count >= n


# March 20, 2023

'''

# Kunal Wadhwa

'''