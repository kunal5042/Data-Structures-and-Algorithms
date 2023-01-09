# Question: https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# Medium

from typing import Optional, List
from collections import defaultdict
from heapq import heappop, heappush
from collections import Counter
class Solution:
    # O(n) Time and O(n) Space
    def isPossible(self, nums: List[int]) -> bool:
        counts      = Counter(nums)
        can_be_used = Counter()
        
        for ele in nums:
            # if this element is already a part of a subsequence
            if counts[ele] == 0: continue
                
            # is this element required by any other subsequence, to extend it
            if can_be_used[ele] > 0:
                can_be_used[ele]     -= 1
                can_be_used[ele + 1] += 1
                
            else:
                # can this element start it's own subsequence
                if counts[ele+1] > 0 and counts[ele+2] > 0:
                    counts[ele+1] -= 1
                    counts[ele+2] -= 1
                    can_be_used[ele + 3] += 1
                else:
                    # if not, return False
                    return False
            
            # this element has been added to an existing subsequence
            # or, it created it's own subsequence
            # either way
            counts[ele] -= 1
            
        return True

    # Solved recently
    # O(n) time and O(n) space
    def isPossible(self, nums: List[int]) -> bool:
        hashmap = defaultdict(list)
        
        for num in nums:
            if num not in hashmap:
                heappush(hashmap[num+1], 1)
            else:
                length = heappop(hashmap[num])
                if len(hashmap[num]) == 0:
                    del hashmap[num]
                heappush(hashmap[num+1], length+1)
                
        for _, lengths in hashmap.items():
            for length in lengths:
                if length < 3:
                    return False
                
        return True

'''

# Kunal Wadhwa

'''