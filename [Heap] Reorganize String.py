# Question: https://leetcode.com/problems/reorganize-string/

from typing import Optional, List

from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap   = [(-freq, char) for char, freq in counts.items()]
        heapq.heapify(heap)
        
        result = ''
        prev   = None
        
        while prev or len(heap) > 0:
            if prev and len(heap) <= 0:
                return ''
            
            freq, char = heapq.heappop(heap)
            result    += char
            freq      += 1
            
            if prev:
                heapq.heappush(heap, prev)
                prev = None
            
            if freq != 0:
                curr = (freq, char)
                prev = curr
                
        
        return result

# Kunal Wadhwa
