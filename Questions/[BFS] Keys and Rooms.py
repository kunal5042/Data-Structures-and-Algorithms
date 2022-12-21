# Question: https://leetcode.com/problems/keys-and-rooms/
# Medium
from typing import Optional, List
from collections import deque

class Solution:
    # O(n + e) time and O(n) space
    # where n is the number of rooms and e is the number of keys
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set()
        
        while len(queue) != 0 and len(visited) != len(rooms):
            unlocked_room = queue.popleft()
            
            if unlocked_room in visited:
                continue
                
            visited.add(unlocked_room)
            
            for key_to_room in rooms[unlocked_room]:
                if key_to_room in visited:
                    continue
                queue.append(key_to_room)
                
        return len(visited) == len(rooms)


# December 20, 2022

'''

# Kunal Wadhwa

'''