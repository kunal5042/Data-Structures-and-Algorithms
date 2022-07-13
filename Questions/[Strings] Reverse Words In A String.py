# Question: https://leetcode.com/problems/reverse-words-in-a-string/

from typing import Optional, List

class Solution:
    # O(n) Time and Space: where n is the length of the input string
    def reverseWords(self, string: str) -> str:
        """Takes a string containing uppercase, lowercase, digits and spaces.
        Reverses the words in the string and returns this new string.
        A word is defined as a sequence of non-space characters
        """
        
        # extract words
        _list = string.strip().split(' ')
        
        # reverse in place
        def reverse(start: int, end: int, iterable: List[str]) -> None:
            while start < end:
                iterable[start], iterable[end] = iterable[end], iterable[start]
                start += 1
                end   -= 1
            return
        
        # remove extra spaces
        def clean_spaces(string : str) -> str:
            cleaned = string[0]
            for idx in range(1, len(string)):
                current, previous = string[idx], string[idx-1]
                if current == ' ' and previous == ' ':
                    continue
                else:
                    cleaned += current
            return cleaned
        
        reverse(0, len(_list)-1, _list)
        return clean_spaces(" ".join(_list))
'''

# Kunal Wadhwa

'''