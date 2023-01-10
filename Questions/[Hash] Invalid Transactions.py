# Question: https://leetcode.com/problems/invalid-transactions/
# Medium
from typing import Optional, List

class Transaction:
    def __init__(self, name, time, amount, city):
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
    
    def __str__(self):
        return ",".join([self.name, str(self.time), str(self.amount), self.city])
        
class Solution:
    # O(n*n) time and O(n) space
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hashmap = {}
        invalid = []
        
        for data in transactions:
            name, time, amount, city = data.split(',')
            transaction_object = Transaction(name, time, amount, city)
            if name not in hashmap:
                hashmap[name] = []
                
            hashmap[name].append(transaction_object)
            
        # we basically check if the current transaction is valid or not
        # and we do this for every transaction
        # thereby avoiding any duplicates and getting the result in desired format
        for data in transactions:
            name, time, amount, city = data.split(',')
            if int(amount) > 1000:
                invalid.append(name+','+time+','+amount+','+city)
                continue
            
            if name in hashmap:
                for tobject in hashmap[name]:
                    if city != tobject.city and abs(int(time)-tobject.time) <= 60:
                        invalid.append(name+','+time+','+amount+','+city)
                        break
        
        return invalid
                


# January 10, 2023

'''

# Kunal Wadhwa

'''