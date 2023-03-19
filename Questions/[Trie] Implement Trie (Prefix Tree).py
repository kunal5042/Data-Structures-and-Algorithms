# Question: https://leetcode.com/problems/implement-trie-prefix-tree/
# Medium


class Trie:
    def __init__(self):
        # The symbol used to mark the end of a word.
        self.end_symbol = "$"
        # The root node of the trie.
        self.root = {}

    def insert(self, word: str) -> None:
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

    def startsWith(self, prefix: str) -> bool:
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

# Overall, this is an implementation of a Trie data structure, which is used to efficiently store and search for strings. Here are some specific comments on each method:

# __init__(self): This method initializes a new Trie object. It sets the end symbol used to mark the end of a word and creates the root node of the trie, which is an empty dictionary.

# insert(self, word: str) -> None: This method inserts a new word into the trie. It starts at the root node and iterates over each character in the word. For each character, it checks if there is a child node for that character. If there is not, it creates a new child node. It then moves down to the child node and repeats the process for the next character. Once it reaches the end of the word, it marks the end of the word by setting the end symbol on the final node.

# search(self, word: str) -> bool: This method searches for a word in the trie. It starts at the root node and iterates over each character in the word. For each character, it checks if there is a child node for that character. If there is not, the word is not in the trie and the method returns False. If there is a child node, it moves down to the child node and repeats the process for the next character. Once it reaches the end of the word, it checks if the end symbol is set on the final


# March 19, 2023

'''

# Kunal Wadhwa

'''