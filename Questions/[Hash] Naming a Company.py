# Question: https://leetcode.com/problems/naming-a-company/
# Hard

from string import ascii_lowercase
from typing import List

class Solution:
    # O(n * m) time and O(n * m) space
    # where n is the length of ideas and m is the length of longest word
    def distinctNames(self, ideas: List[str]) -> int:
        indices = {char:idx for idx, char in enumerate(ascii_lowercase)}
        get_group_id = lambda char: indices[char]
    
        # given all ideas are unique, hence we can safely use set
        # to reduce lookup time complexity
        groups = [set() for _ in range(26)]
        
        for idea in ideas:
            initial = idea[0]
            suffix = idea[1:]
            
            # allot group
            groups[get_group_id(initial)].add(suffix)
            
        answer = 0
        for idx in range(26):
            # empty
            if len(groups[idx]) == 0: continue
                
            for jdx in range(idx+1, 26):
                # empty
                if len(groups[jdx]) == 0: continue
                    
                # every suffix in g1 can form a pair with every suffix in g2
                # exclude the common suffixes: doesn't satisfy c3
                group1 = groups[idx]
                group2 = groups[jdx]
                common = group1.intersection(group2)
                
                answer += 2 * (
                    (len(group1) - len(common))
                    *
                    (len(group2) - len(common)) 
                )
                
        return answer
                


# February 09, 2023

'''

# Kunal Wadhwa

'''