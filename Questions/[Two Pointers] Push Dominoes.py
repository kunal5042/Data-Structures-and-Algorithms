# Question: https://leetcode.com/problems/push-dominoes/

from typing import Optional, List

class Solution:
    # O(n) Time and O(n) Space
    # Space can be optimized to O(1) by not converting the dominoes str to a list
    # And by instead building a new resultant str
    # Will do that later sometime!
    def pushDominoes(self, dominoes: str) -> str:
        
        # if domino stands still i.e is a dot
        # search for the first right domino to the left
        # and first left domino to the right
        # if a right domino is not found but left domino is found: current domino falls to left
        # and vice versa
        # if both dominos are found, move to centre
        
        def get_right_domino(start) -> int:
            """Returns the index of the first right domino to the left"""
            _iter = start - 1
            right_domino = None
            
            while _iter >= 0:
                if dominoes[_iter] == 'L':
                    break
                if dominoes[_iter] == 'R':
                    return _iter
                _iter -= 1
                
            return right_domino
        
        
        def get_left_domino(start) -> int:
            """Returns the index of the first left domino to the right"""
            _iter = start + 1
            left_domino = None
            
            while _iter < len(dominoes):
                if dominoes[_iter] == 'R':
                    break
                if dominoes[_iter] == 'L':
                    return _iter
                _iter += 1
                
            return left_domino
        
        
        # for editing
        dominoes = [char for char in dominoes]
        for idx in range(len(dominoes)):
            if dominoes[idx] == '.':
                right_dom = get_right_domino(idx)
                left_dom  = get_left_domino(idx)
                
                if left_dom  is not None and right_dom is None: dominoes[idx] = 'L'
                if right_dom is not None and left_dom  is None: dominoes[idx] = 'R'
                    
                if left_dom is not None and right_dom is not None:
                    right, left = right_dom, left_dom
                    
                    # when right == left
                    # that domino will be balanced
                    while right < left:
                        dominoes[right] = 'R'
                        dominoes[left]  = 'L'
                        right += 1
                        left  -= 1
                        
        return "".join(dominoes)
'''

# Kunal Wadhwa

'''