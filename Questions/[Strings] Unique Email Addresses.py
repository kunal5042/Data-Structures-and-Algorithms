# Question: https://leetcode.com/problems/unique-email-addresses/
# Easy
from typing import Optional, List

class Solution:
    # O(n * m) time and O(n) space
    # where n is the number of emails
    # and m is the length of the largest email 
    # where largest email has the maximum number of characters
    
    def numUniqueEmails(self, emails: List[str]) -> int:
        _hash = set()
        
        for email in emails:
            local_name = []
            for idx in range(len(email)):
                if email[idx] == '@': break
                if email[idx] == '.': continue
                local_name.append(email[idx])
            
            domain_name = email[idx+1:]
            _hash.add(''.join(local_name).split('+')[0] + '@' + domain_name)
            
        return len(_hash)


# December 25, 2022

'''

# Kunal Wadhwa

'''