# Question: https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/description/
# Medium


class Solution:
    # O(n) time and O(1) space
    def longestSemiRepetitiveSubstring(self, string: str) -> int:
        longest = 1
        count = 0
        start = 0

        for end in range(len(string)):
            if end > 0 and string[end-1] == string[end]:
                count += 1

            while count > 1:
                if end > start and string[start] == string[start+1]:
                    count -= 1

                start += 1

            longest = max(longest, end - start + 1)

        return longest


# June 16, 2023

'''

# Kunal Wadhwa

'''