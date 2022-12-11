# Question: https://leetcode.com/problems/design-a-text-editor/
# Hard
# 
from typing import Optional, List

class TextEditor:

    def __init__(self) -> 'TextEditor':
        self.s = ''
        self.cursor = 0

    # O(n) Time and Space
    def addText(self, text: str) -> None:
        self.s = self.s[:self.cursor] + text + self.s[self.cursor:]
        self.cursor += len(text)

    # O(n) Time and Space
    def deleteText(self, k: int) -> int:
        new_cursor = max(0, self.cursor - k)
        no_of_chars = k if self.cursor - k >= 0 else self.cursor
        self.s = self.s[:new_cursor] + self.s[self.cursor:]
        self.cursor = new_cursor
        return no_of_chars

    # O(n) Time and Space
    def cursorLeft(self, k: int) -> str:
        self.cursor = max(0, self.cursor - k)
        start = max(0, self.cursor-10)
        return self.s[start:self.cursor]

    # O(n) Time and Space
    def cursorRight(self, k: int) -> str:
        self.cursor = min(len(self.s), self.cursor + k)
        start = max(0, self.cursor - 10)
        return self.s[start:self.cursor]
        

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
'''

# Kunal Wadhwa

'''