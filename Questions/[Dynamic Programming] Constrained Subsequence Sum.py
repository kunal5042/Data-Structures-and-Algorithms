# Question: https://leetcode.com/problems/constrained-subsequence-sum/
# Hard

import math
from collections import deque
from typing import List

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # maximum sum of a non-empty subsequence
        # subsequence condition
        # every consecutive integers in the subsequence
        # i1, i2, i3, i4, ..... in
        # in - in-1 <= k holds true for every consecutive pair

        # open questions
        # can the value of k be less than 1 ? no
        # can array be empty? no

        # how to maximise the sum?
        # exclude as many negative numbers as possible
        # can we exclude all negative numbers? no
            # why can't we exclude all negative numbers?
            # it's because of the condition in - in-1 <= k
            # so k decides how far we can move before we have to include another number
            # what do we do? we minimise the negative number if it has to be included
            # when does it have to be included?
                # when including it justifies the cost
                    # that happens when it allows us to move ahead and add more +ve nos
                    # can we define it using math?
                    # nums = [4 ,-10 ,-1 ,-11 ,-1 ,-24 ,-1 ,100] , k = 2

        # approach - 1
        # init global max subsequence sum as -inf
        # start from every number, init subsequence sum as the current number
        # keep track of the largest number in the next i + k numbers
        # add that number to subsequence sum, follow the same process for this number
        # follow this process till we can't move further
        # compare it with global max subsequence sum
        # time - O(n*n)

        # approach - 2
        # we initialize an array dp to store the largest subsequence sum that can attained
        # if the current element is the last element of the subsequence
        # we initialize dp array with len equal to that of nums with 0th element as same
        # every step of the array forward
        # we traverse back i - k positions in j, and keep of track of max(dp[i], dp[i] + dp[i-j])
        # in the end we return max(dp)
        # time - O(n*k)

        # approach - 3
        # init global max subsequence sum as -inf
        # init a max heap with first element, and it's index
        # as we move forward in the nums, we check if we should be adding top of max heap to curr
        # we only add if top > 0 and top's index <= cur - k
        # we add the top to cur sum and add the final sub seq sum to heap
        # we keep track of global max subsequence sum and do this for all remaining elements in nums
        # in the end, return global max subsequence sum
        # time - O(n*log(n))

        # approach - 4
        # same as approach 3 logically but instead of using heap we use a sorted list or a red black tree
        # where the current size is more than window size
        # we remove current index - k from sorted list efficiently
        # keeping space to at max k and that's why adding more ele to the DS takes O(log(k))
        # bringing total time complexity to
        # time - O(n*log(k))

        # approach - 5
        # we can use a monotonic decreasing double ended queue to store the max sub seq sum dp[j] at front
        # and as we traverse forward we add dp[i] to the back in monotonic fashion
        # and remove elements out of the window from the front
        # using this we can always get the max sub seq sum before current in O(1)
        # time - O(n)
        
        queue = deque()
        dp = [0 for _ in range(len(nums))]
        
        for idx in range(len(nums)):
            # removing elements out of window
            while len(queue) != 0 and idx - queue[0] > k:
                queue.popleft()
                
            # maximum subseq sum ending at current element
            delta = dp[queue[0]] if len(queue) != 0 else 0
            dp[idx] = nums[idx] + delta
            
            # inserting in monotonic decreasing fashion
            while len(queue) != 0 and dp[queue[~0]] < dp[idx]:
                queue.pop()
                
            if dp[idx] > 0: queue.append(idx)
                
        return max(dp)


# October 21, 2023

'''

# Kunal Wadhwa

'''