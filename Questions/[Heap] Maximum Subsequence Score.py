# Question: https://leetcode.com/problems/maximum-subsequence-score/description/
# Medium

from heapq import heappush, heappop, heapify

class Solution:
    # O(n*log(n)) time and O(n) space
    def maxScore(self, nums1, nums2, k):
        # Combine nums1 and nums2 into pairs
        pairs = [(a, b) for a, b in zip(nums1, nums2)]

        # Sort pairs by nums2 in decreasing order
        pairs.sort(key=lambda x: -x[1])

        # Use a min-heap to maintain the top k elements
        top_k_heap = [x[0] for x in pairs[:k]]
        heapify(top_k_heap)

        # Calculate the initial sum of top k elements
        top_k_sum = sum(top_k_heap)

        # Calculate the score of the first k pairs
        answer = top_k_sum * pairs[k - 1][1]

        # Iterate over the remaining pairs
        for i in range(k, len(nums1)):
            # Remove the smallest element from the top k elements
            top_k_sum -= heappop(top_k_heap)

            # Add the current element to the top k elements
            top_k_sum += pairs[i][0]
            heappush(top_k_heap, pairs[i][0])

            # Update the answer if necessary
            answer = max(answer, top_k_sum * pairs[i][1])

        return answer



# May 25, 2023

'''

# Kunal Wadhwa

'''