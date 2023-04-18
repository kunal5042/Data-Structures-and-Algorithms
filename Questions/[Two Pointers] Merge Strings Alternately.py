# Question: https://leetcode.com/problems/merge-strings-alternately/
# Easy


class Solution:
    # O(n+m) time and O(n+m) space
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        iter1, iter2 = 0, 0
        flag = True
        
        while iter1 < len(word1) and iter2 < len(word2):
            if flag is True:
                merged.append(word1[iter1])
                iter1 += 1
            else:
                merged.append(word2[iter2])
                iter2 += 1
                
            flag = not flag
        
        while iter1 < len(word1):
            merged.append(word1[iter1])
            iter1 += 1
            
        while iter2 < len(word2):
            merged.append(word2[iter2])
            iter2 += 1
            
        return "".join(merged)
            


# April 18, 2023

'''

# Kunal Wadhwa

'''