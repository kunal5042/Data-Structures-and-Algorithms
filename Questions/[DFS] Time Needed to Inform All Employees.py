# Question: https://leetcode.com/problems/time-needed-to-inform-all-employees/description/
# Medium

from collections import defaultdict
from typing import List

class Solution:
    # O(n) time and O(n) space
    def get_graph(self, adjacency_list):
        graph = defaultdict(list)
        for sub_ordinate_id, manager_id in enumerate(adjacency_list):
            graph[manager_id].append(sub_ordinate_id)
        return graph 

    # O(n) time and O(h) space
    def get_maximum_spread_time(self, source, graph, inform_time):
        base_time = inform_time[source]
        next_level_time = 0
        for sub_ordinate_id in graph[source]:
            next_level_time = max(
                next_level_time,
                self.get_maximum_spread_time(sub_ordinate_id, graph, inform_time)
            )
        return base_time + next_level_time

    # O(n) time and O(n) space
    def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
        return self.get_maximum_spread_time(
            head_id,
            self.get_graph(manager),
            inform_time
        )


# June 03, 2023

'''

# Kunal Wadhwa

'''