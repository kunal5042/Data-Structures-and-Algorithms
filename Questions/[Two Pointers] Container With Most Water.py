# Question: https://leetcode.com/problems/container-with-most-water

class Solution:
    # O(n) Time and O(1) Space
    def maxArea(self, height: List[int]) -> int:
        if len(height) == 0: return 0
        
        left, right  = 0, len(height)-1
        result_water = 0
        
        while left < right:
            current_water = (right-left) * min(height[left], height[right])
            result_water  = max(result_water, current_water)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return result_water
    

    # O(n^2) Time and O(1) Space
    def max_area(self, height: List[int]) -> int:
        if len(height) == 0: return 0
        
        reswater = 0
        reslower = None
        
        for idx in range(len(height)):
            if reslower is not None and height[idx] < reslower:
                continue
                
            left_pillar = height[idx]
            count = 0
            for jdx in range(idx+1, len(height)):
                count += 1
                right_pillar = height[jdx]
                current_water = (min(left_pillar, right_pillar)) * count
                if current_water > reswater:
                    reslower = min(left_pillar, right_pillar)
                    reswater = current_water
                    
        return reswater
    
# Kunal Wadhwa