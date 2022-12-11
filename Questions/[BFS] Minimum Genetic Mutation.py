# Question: https://leetcode.com/problems/minimum-genetic-mutation/
# Medium
from typing import Optional, List

from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        
        # quick escape
        if end not in bank: return -1
        
        def get_mutations(gene):
            mutations = []
            for idx in range(len(gene)):
                for char in "ACGT":
                    # can't mutate
                    if gene[idx] == char: continue
                        
                    # possible mutations
                    mutation = gene[:idx] + char + gene[idx+1:]
                    
                    # can use this mutation
                    if mutation in bank:
                        mutations.append(mutation)
                        
                        # for optimization
                        bank.remove(mutation)
            return mutations
        
        queue = deque([(start, 0)])
        
        while len(queue) != 0:
            gene, mutations_performed = queue.popleft()
            
            # successfully mutated
            if gene == end: return mutations_performed
            
            for mutated_gene in get_mutations(gene):
                # if already fully mutated, no need to process the remaining queue
                if mutated_gene == end: return mutations_performed + 1
                
                queue.append((mutated_gene, mutations_performed + 1))
                
        # exhausted all possible mutations
        # failed to mutate completely
        return -1
'''

# Kunal Wadhwa

'''