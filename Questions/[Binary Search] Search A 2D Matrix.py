# Question: https://leetcode.com/problems/search-a-2d-matrix/
# Medium
# To Do: Binary Search entire matrix at each iteration
from typing import Optional, List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Given a sorted 2d matrix of integers and an integer target.
        Returns true if target is found in the matrix.
        """
        result = False
        
        # find the row using binary search
        def find_row():
            nonlocal result
            row = None
            
            left, right = 0, len(matrix)-1
            
            while left <= right:
                middle = (left + right) // 2
                
                # if row start == target. Stop
                if matrix[middle][0] == target:
                    result = True
                    return row
                
                if matrix[middle][0] < target:
                    row = middle
                    left = middle + 1
                    
                else:
                    right = middle - 1
                    
            return row
        
        def binary_search(row):
            # if row start was target or no row was found
            if result is True: return True
            if row is None   : return False
            
            left, right = 0, len(matrix[row])-1

            while left <= right:
                middle = (left + right) // 2
                
                if matrix[row][middle] == target:
                    return True
                
                if matrix[row][middle] > target:
                    right = middle - 1
                else:
                    left  = middle + 1
                    
            return False
        
        
        return binary_search(find_row())
    
'''

# Kunal Wadhwa

'''