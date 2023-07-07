# Question: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/
# Medium

from collections import deque

class Solution:
    def get_max_substring(self, array, _default, k):
        result = 0
        change_indices = deque()
        start = -1
        for end in range(len(array)):
            char = array[end]
            if char == _default:
                result = max(result, end - start)
                continue

            if len(change_indices) == k:
                start = change_indices.popleft()

            change_indices.append(end)

            result = max(result, end - start)

        return result

    # O(n) time and O(k) space
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        return max(
            self.get_max_substring(answerKey, "F", k),
            self.get_max_substring(answerKey, "T", k)
        )


# July 07, 2023

'''

# Kunal Wadhwa

'''