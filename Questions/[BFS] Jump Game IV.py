# Question: https://leetcode.com/problems/jump-game-iv/
# Hard

from typing import List

class Solution:
    # O(n) time and O(n) space
    def minJumps(self, arr: List[int]) -> int:
        """
        Given an array of integers arr, return the minimum number of jumps to reach the last index of the array.
        In one jump, you can move to an index i + 1, i - 1, or j where arr[i] == arr[j] and i != j.
        """
        n = len(arr)
        if n <= 1:
            return 0

        # Create a dictionary to represent the graph with keys as values in the array
        # and values as a list of indices where the key appears in the array
        value_to_indices = {}
        for i in range(n):
            value = arr[i]
            if value in value_to_indices:
                value_to_indices[value].append(i)
            else:
                value_to_indices[value] = [i]

        # Start BFS from the first index of the array
        current_indices = [0]
        visited_indices = {0}
        jumps = 0

        # When the current layer exists
        while current_indices:
            next_indices = []

            # Iterate through the nodes in the current layer
            for current_index in current_indices:
                # If the last index is reached, return the number of jumps
                if current_index == n - 1:
                    return jumps

                # Check the same value jumps
                for next_index in value_to_indices[arr[current_index]]:
                    if next_index not in visited_indices:
                        visited_indices.add(next_index)
                        next_indices.append(next_index)

                # Clear the list to prevent redundant search
                value_to_indices[arr[current_index]].clear()

                # Check the neighboring indices
                for next_index in [current_index - 1, current_index + 1]:
                    if 0 <= next_index < len(arr) and next_index not in visited_indices:
                        visited_indices.add(next_index)
                        next_indices.append(next_index)

            current_indices = next_indices
            jumps += 1

        # If the last index is not reachable, return -1
        return -1

# Time complexity analysis:
# Creating the value_to_indices dictionary takes O(n) time and space.
# The while loop iterates at most n times where n is the length of the array.
# The for loop inside the while loop can add at most two new indices to the next layer,
# so the total number of iterations of the for loop is at most 2n.
# The time complexity of adding and accessing elements in a dictionary and a set
# is O(1) on average, so the overall time complexity of the algorithm is O(n).



# March 05, 2023

'''

# Kunal Wadhwa

'''