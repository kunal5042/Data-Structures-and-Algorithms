# Question: https://leetcode.com/problems/sort-integers-by-the-power-value/
# Medium

from typing import Optional, List

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        """Returns the kth position integer from a sorted powerlist of range [lo:hi+1]"""
        LOW, HIGH = lo, hi
        minsteps  = [None for _ in range(HIGH+1)]
        position  = k
        
        for idx in range(1, HIGH+1):
            self.minimum_steps_to_one(idx, minsteps)
            
        power_list = []
        for idx in range(LOW, HIGH+1):
            power_list.append((idx, minsteps[idx]))
            
        power_list.sort(key=lambda x: x[1])
        return power_list[position-1][0]

            
    def minimum_steps_to_one(self, number: int, minsteps: List[int]) -> int:
        """Returns the minimum number of steps to convert a number into 1"""
        number_ = number
        steps = 0
        while number != 1:
            if number < len(minsteps) and minsteps[number] is not None:
                steps += minsteps[number]
                break

            if number % 2 == 0:
                number = number // 2
            else:
                number = (3 * number) + 1
                
            steps += 1
            
        minsteps[number_] = steps
        return steps
'''

# Kunal Wadhwa


'''