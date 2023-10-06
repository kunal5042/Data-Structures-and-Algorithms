# Question: https://leetcode.com/problems/integer-break/
# Medium


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        
        dp = [0] * (n + 1)

        # Set base cases
        for i in [1, 2, 3]:
            dp[i] = i
            
        for num in range(4, n + 1):
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp[num - i])
            
            dp[num] = ans
        
        return dp[n]
    
    def integerBreak(self, n: int) -> int:
        # n can't be smaller than 2
        
        # maximise the product of the sum
        # what maximises the product?
        # we need largest separation with largest numbers
        # 2 - 1 * 1
        # 3 - 1 * 2
        # 4 - 2 * 2
        # 5 - 2 * 3
        # 6 - 3 * 3
        # 7 - 3 * 4
        # 8 - 3 * 3 * 2
        # 9 - 3 * 3 * 3
        # 10 - 3 * 3 * 4
        # 11 - 3 * 3 * 3 * 2
        # 12 - 3 * 3 * 3 * 3
        # 13 - 3 * 3 * 3 * 4
        # 14 - 3 * 3 * 3 * 3 * 2
        result = [0, 0, 1, 2, 4, 6]
        if n < len(result):
            return result[n]
        
        if n % 3 == 0:
            return 3 ** (n // 3)
        
        if n % 3 == 1:
            return (3 ** ((n // 3)-1)) * 4
        
        return 3 ** (n // 3) * 2


# October 06, 2023

'''

# Kunal Wadhwa

'''