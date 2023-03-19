# Question: https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Medium


class WordDictionary:

    def __init__(self):
        # Initialize the trie with an empty root node and an end symbol to mark the end of a word
        self.root = {}
        self.end_symbol = "kunal"

    def addWord(self, word: str) -> None:
        # Start at the root node
        node = self.root
        # Traverse the trie, adding new nodes for each character in the word
        for character in word:
            if character not in node:
                node[character] = {}
            node = node[character]
        # Add the end symbol to mark the end of the word
        node[self.end_symbol] = {}

    def search(self, word: str) -> bool:
        # Helper function to perform a depth-first search of the trie
        def helper(node, idx):
            # If we've reached the end of the word, check if the end symbol is in the current node
            if idx == len(word):
                return self.end_symbol in node
            # If the current character is a dot, try all possible paths from the current node
            if word[idx] == '.':
                for _id, sub_node in node.items():
                    if helper(sub_node, idx+1) is True:
                        return True
                return False
            # If the current character is a letter, traverse down the corresponding path
            elif word[idx] in node:
                return helper(node[word[idx]], idx+1)
            # If the current character is not in the trie, the word is not in the trie
            else:
                return False
        # Start the search at the root node
        return helper(self.root, 0)


# March 19, 2023

'''

# Kunal Wadhwa

'''