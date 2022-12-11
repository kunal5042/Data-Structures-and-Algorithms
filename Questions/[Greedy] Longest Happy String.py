# Question: https://leetcode.com/problems/longest-happy-string/
# Medium
from typing import Optional, List

class Solution:
    # O(n) Time and O(1) Space
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for freq, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if freq != 0: heap.append((freq, char))
                
        heapify(heap)
        string = ''
        
        while len(heap) != 0:
            freq, char = heappop(heap)
                
            if len(string) < 2:
                string += char
                freq += 1
                if freq != 0: heappush(heap, (freq, char))
                continue
            
            if string[-2:] != char+char:
                string += char
                freq += 1
                    
            else:
                if len(heap) == 0: break
                nfreq, nchar = heappop(heap)
                string += nchar
                nfreq += 1
                if nfreq != 0: heappush(heap, (nfreq, nchar))
                    
            if freq != 0: heappush(heap, (freq, char))
                    
        return string
'''

# Kunal Wadhwa

'''