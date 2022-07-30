# Question: https://leetcode.com/problems/simplify-path/

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    def simplifyPath(self, path: str) -> str:
        """Converts absolute path into canonical path.
        Returns the canonical path
        """
        stack = []
        
        for directory in path.split('/'):
            if directory == '.' or directory == '':
                continue
            
            if directory == '..' and len(stack):
                stack.pop()
                continue
                
            if directory != '..':
                stack.append(directory)
            
            
        return '/' + '/'.join(stack)
'''

# Kunal Wadhwa

'''