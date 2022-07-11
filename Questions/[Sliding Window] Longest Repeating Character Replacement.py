# Question: https://leetcode.com/problems/longest-repeating-character-replacement/

from typing import Optional, List

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Takes a string s and an integer k
        Returns the length of longest substring containing the same letter after replacing 
        maximum of k chars in the substring
        """
        counts = Counter()
        start  = 0
        result = 1
        
        for end in range(len(s)):
            current_char          = s[end]
            counts[current_char] += 1
            window_size           = end - start + 1
            
            replacements = window_size - counts.most_common(1)[0][1]
            
            while replacements > k:
                char_to_remove = s[start]
                counts[char_to_remove] -= 1
                start += 1
                replacements -= 1
                
            new_window_size = end - start + 1
            result = max(result, new_window_size)
            
        return result
                
    
    def characterReplacement_BRUTE_FORCE(self, s: str, k: int) -> int:
        result = 1
        for idx in range(len(s)):
            replacements = k
            previous = s[idx]
            
            for jdx in range(idx+1, len(s)):
                if s[jdx] != previous:
                    if replacements == 0: break
                    replacements -= 1
                    
                if replacements == 0:
                    result = max(result, jdx-idx+1)
        return result
'''

# Kunal Wadhwa

'''