# Question: https://leetcode.com/problems/insert-delete-getrandom-o1/
# Medium
from typing import Optional, List

class RandomizedSet:
    # O(1) time for all methods
    def __init__(self):
        self.container = set()

    def insert(self, val: int) -> bool:
        if val in self.container:
            return False
        self.container.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.container:
            return False
        self.container.discard(val)
        return True

    def getRandom(self) -> int:
        return random.sample(self.container, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# November 29, 2022

'''

# Kunal Wadhwa

'''