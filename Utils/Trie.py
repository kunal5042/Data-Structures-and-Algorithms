# Question: https://leetcode.com/problems/implement-trie-prefix-tree/
# Medium

class Trie:
    """
    This class implements a Trie data structure, which is used to efficiently store and search for strings.

    Attributes:
        end_symbol (str): The symbol used to mark the end of a word.
        root (dict): The root node of the trie.

    Methods:
        __init__ (self): Initializes a new Trie object.
        insert (self, word: str) -> None: Inserts a new word into the trie.
        search (self, word: str) -> bool: Searches for a word in the trie.
        starts_with (self, prefix: str) -> bool: Checks if a prefix is present in the trie.
    """

    def __init__(self):
        """
        Initializes a new Trie object.
        """
        # The symbol used to mark the end of a word.
        self.end_symbol = "$"
        # The root node of the trie.
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a new word into the trie.

        Args:
            word (str): The word to insert.
        """
        # Start from the root node.
        node = self.root
        # Iterate over each character in the word.
        for char in word:
            # If the character is not already in the trie,
            # add a new node for it.
            if char not in node:
                node[char] = {}
            # Move down to the next level in the trie.
            node = node[char]
        # Mark the end of the word by setting the end symbol on the final node.
        node[self.end_symbol] = True

    def search(self, word: str) -> bool:
        """
        Searches for a word in the trie.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word is present in the trie, False otherwise.
        """
        # Start from the root node.
        node = self.root
        # Iterate over each character in the word.
        for char in word:
            # If the character is not in the trie, the word is not in the trie.
            if char not in node:
                return False
            # Move down to the next level in the trie.
            node = node[char]
        # If we reach the end of the word and the end symbol is set on the final node,
        # the word is in the trie. Otherwise, it is not.
        return self.end_symbol in node

    def starts_with(self, prefix: str) -> bool:
        """
        Checks if a prefix is present in the trie.

        Args:
            prefix (str): The prefix to check.

        Returns:
            bool: True if the prefix is present in the trie, False otherwise.
        """
        # Start from the root node.
        node = self.root
        # Iterate over each character in the prefix.
        for char in prefix:
            # If the character is not in the trie, the prefix is not in the trie.
            if char not in node:
                return False
            # Move down to the next level in the trie.
            node = node[char]
        # If we reach the end of the prefix, the prefix is in the trie.
        return True

# March 19, 2023

'''

# Kunal Wadhwa

'''