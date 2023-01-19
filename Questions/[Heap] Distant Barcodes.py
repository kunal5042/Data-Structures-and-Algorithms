# Question: https://leetcode.com/problems/distant-barcodes/
# Medium
from typing import Optional, List

class Solution:
    # O(n * log(n)) time and O(n) space
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        heap = []
        
        for num, freq in Counter(barcodes).items():
            heap.append((-freq, num))
            
        heapify(heap)
        result = []
        while len(heap) != 0:
            freq, num = heappop(heap)
            if freq == 0: continue
            
            if len(result) == 0:
                freq += 1
                result.append(num)
                heappush(heap, (freq, num))
                continue
                
            if result[~0] == num:
                freq2, num2 = heappop(heap)
                freq2 += 1
                result.append(num2)
                heappush(heap, (freq2, num2))
                heappush(heap, (freq, num))
                continue
                
            freq += 1
            result.append(num)
            heappush(heap, (freq, num))
        
        return result


# January 19, 2023

'''

# Kunal Wadhwa

'''