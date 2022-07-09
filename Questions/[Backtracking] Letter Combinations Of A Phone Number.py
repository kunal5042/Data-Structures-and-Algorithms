# Question: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import Optional, List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits): return []
        result = []
        _map = {
		
        '1': '1',    '2': 'abc',   '3': 'def', 
		'4': 'ghi',  '5': 'jkl',   '6': 'mno',
		'7': 'pqrs', '8': 'tuv',   '9': 'wxyz',
					 '0': '0'
        }
        
        def combinations(num_idx, this_combination):
            if num_idx == len(digits):
                result.append(this_combination)
                return
                
            num = digits[num_idx]
            for replacement in _map.get(num, []):
                combinations(num_idx+1, this_combination + replacement)
            
            return result
        
        return combinations(0, '')
'''

# Kunal Wadhwa

'''