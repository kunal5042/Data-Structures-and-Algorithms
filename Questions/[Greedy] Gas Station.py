# Question: https://leetcode.com/problems/gas-station/

from typing import Optional, List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = total_gas = current_gas = 0
        
        for idx in range(len(gas)):
            station_gas  = gas[idx]
            station_cost = cost[idx]
            
            total_gas   += station_gas - station_cost
            current_gas += station_gas - station_cost
            
            if current_gas < 0:
                start = idx + 1
                current_gas = 0
            
        return start if total_gas >= 0 else -1
'''

# Kunal Wadhwa

'''