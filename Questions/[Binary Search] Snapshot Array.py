# Question: https://leetcode.com/problems/snapshot-array/description/
# Medium

from bisect import bisect_right

class SnapshotArray:

    def __init__(self, length: int):
        self.snap_count = 0
        self.container = [[(0, 0)] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        self.container[index].append((self.snap_count, val))
        
    def snap(self) -> int:
        self.snap_count += 1
        return self.snap_count - 1

    # O(log(n)) time and O(n) space
    def get(self, index: int, snap_id: int) -> int:
        idx = bisect_right(self.container[index], (snap_id, float('inf')))
        return self.container[index][idx-1][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)


# June 11, 2023

'''

# Kunal Wadhwa

'''