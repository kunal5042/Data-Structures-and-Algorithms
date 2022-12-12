# Question: https://leetcode.com/problems/climbing-stairs/
# Easy

class Solution:
    # O(n) time and O(n) space
    def climbStairs(self, n: int) -> int:
        ways = [0, 1, 2]
        for stairs in range(3, n+1):
            ways.append(
                ways[stairs-1] + ways[stairs-2]
            )

        return ways[n]
    
# Kunal Wadhwa