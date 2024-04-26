# Question: https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/
# Hard


class Solution:
    def __init__(self):
        self.visited = None
        self._str = None
        self.palindromes = 0
        self.min_palindrome_length = None

    def markVisited(self, start: int, end_inclusive: int):
        for idx in range(start, end_inclusive+1):
            self.visited[idx] = True

    def findPalindrome(self, is_centre_idx: bool, idx: int):
        left = idx - 1 
        right = idx + 1 if not is_centre_idx else idx

        while left > -1 and right < len(self._str) \
        and self._str[left] == self._str[right] \
        and not self.visited[left] \
        and not self.visited[right]:

            # reached min length
            if right - left + 1 >= self.min_palindrome_length:
                self.markVisited(left, right)
                self.palindromes += 1
                break

            left -= 1
            right += 1

    def maxPalindromes(self, _str: str, k: int) -> int:
        self._str = _str
        self.min_palindrome_length = k
        self.visited = [False for _ in range(len(self._str))]

        if self.min_palindrome_length  == 1:
            return len(self._str)

        for idx in range(len(self._str)):
            self.findPalindrome(True, idx)
            self.findPalindrome(False, idx)

        return self.palindromes


# April 26, 2024

'''

# Kunal Wadhwa

'''