# Question: https://leetcode.com/problems/path-sum-ii
# Medium
# Use backtracking to check all root-to-leaf paths
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # O(n) Time and O(n) Space: where n is the length of the input array
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
        """ Takes in an object of TreeNode and an integer target sum
        Returns a list of every path from the node object to the leaf where path sum 
        equals target sum
        """
        paths = []

        def depth_first_search(node, path, path_sum):
            if not node: return
            if not node.left and not node.right:
                if path_sum + node.val == target_sum:
                    path.append(node.val)
                    paths.append(path.copy())
                    path.pop()
                return

            path.append(node.val)
            depth_first_search(node.left , path, path_sum + node.val)
            depth_first_search(node.right, path, path_sum + node.val)
            path.pop()

            return

        depth_first_search(root, [], 0)
        return paths

        """ Algorithm:
        Explore every path from root to leaf while keeping track of the path sum
        When a leaf is encountered
        if path sum equals target sum
            - Add the current path to the result
        backtrack and explore remaining paths till the entire tree is explored
        """
'''

# Kunal Wadhwa

'''