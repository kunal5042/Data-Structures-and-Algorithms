# Question: https://leetcode.com/problems/longest-string-chain/
# Medium

from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # words
        # array - len shouldn't be 0
        # each element should be of type string 
        # each string should only have lower case letters
        
        # wordA is predecessor of wordB if we can insert excactly one character in wordA without changing ordering of already existing letters
        # such that this insertion results in wordA == wordB is True
        
        # word chain is an array of words where each ith element is a predecessor of jth element
        # such that i == j - 1 and 0 <= i < len(a) and 0 <= j < len(a)
        
        # word chain's length can be 1 or longer
        
        # return the longest word chain from the list of words
        
        # facts
        # every predecessor's length is going to be exactly one less than it's successor 
        
        #
        # given two elements we can find out if the smaller is predecessor to the larger one by comparing char by char with one mismatch allowed
        # this will take O(n+m) time where n is the smaller string and m is the larger string
        
        # we can write the above function let's assume it's contract is below
        # is_predecessor(string a, string b) -> bool
        
        # we can sort the given words by their length in increasing order
        # we'll create an array to store the sub problems results
        # sub problem being if we start from the current word, how many more successors can we have such that they satisfy the word chain condition
        # adding to this sub problem, if we can find another word which is predecessor to this current word (above statement), we can add one to the longest length
        # and so on
        
        # this way we'll loop through the array in O(x^x) time where we'll make comparisons between two strings at every stage of the iteration
        # thereby O(x^x) * O(n * m) time 
        # it will take O(x) space
        
        def is_predecessor(string1, string2):
            if abs(len(string1) - len(string2)) != 1:
                return False
            
            # this will make the assumption that len(string1) <= len(string2) always hold true
            if len(string1) > len(string2):
                string1, string2 = string2, string1
                
            flag = False
            iter1, iter2 = 0, 0
            while iter1 < len(string1) and iter2 < len(string2):
                if string1[iter1] != string2[iter2]:
                    
                    # this has happened before
                    if flag is True:
                        return False
                    
                    # let it happen once
                    flag = True
                    
                    # longer string gets one more chance
                    iter2 += 1
                    
                    continue
                    
                iter1 += 1
                iter2 += 1
                
            return True
        
        if len(words) == 0:
            return 0
        
        subsolutions = {word:1 for word in words}
        
        # this will keep track of the longest chain so that we can save one traversal through subsolutions at the end
        max_tracker = 1
        words.sort(key=len)
        
        for idx in reversed(range(len(words))):
            for jdx in reversed(range(idx+1, len(words))):
                # let's call words[jdx] = A and words[idx] = B
                # here A is asking, can I attach to chain starting from B?
                if is_predecessor(words[idx], words[jdx]) is True:
                    
                    # here A is evaluating, will attaching to this chain will make me part of a larger chain than I currently have?
                    subsolutions[words[idx]] = max(
                        subsolutions[words[jdx]] + 1,
                        subsolutions[words[idx]]
                    )
                    
                    # max tracker keeping track
                    max_tracker = max(max_tracker, subsolutions[words[idx]])
                    
        return max_tracker


# September 23, 2023

'''

# Kunal Wadhwa

'''