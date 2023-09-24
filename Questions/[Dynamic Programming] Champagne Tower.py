# Question: https://leetcode.com/problems/champagne-tower/
# Medium

class Solution:
    def champagneTower(self, poured: int, rownum: int, colnum: int) -> float:
        if poured == 0:
            return 0.0
        
        # Initialize a 2D array to represent the glasses and fill them with zeros.
        glasses = [[0.0] * (i + 1) for i in range(rownum + 1)]
        glasses[0][0] = poured
        
        # Iterate through each row and glass position to calculate the overflow.
        for row in range(rownum):
            for col in range(len(glasses[row])):
                overflow = (glasses[row][col] - 1.0) / 2.0
                if overflow > 0:
                    glasses[row + 1][col] += overflow
                    glasses[row + 1][col + 1] += overflow
        
        # Ensure the value is between 0 and 1 and return the result.
        return min(1.0, glasses[rownum][colnum])


# September 24, 2023

'''

# Kunal Wadhwa

'''