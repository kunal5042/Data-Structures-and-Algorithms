# Question: https://leetcode.com/problems/fraction-to-recurring-decimal/
# Medium
from typing import Optional, List

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # base case, operation simply checks out
        if numerator % denominator == 0:
            return str(numerator // denominator)
        sign = '+'
        if numerator * denominator < 0:
            sign = '-'
        
        # in python, negative division is not as expected
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        # starting point
        result = str(numerator // denominator) + '.'
        numerator %= denominator
        
        # calculation of fraction
        # we noted that once the remainder starts repeating, so does the dividend
        # that allows us to stop
        # otherwise looping stop once the numerator is fully divided
        idx = 0
        fraction = ''
        memo = {numerator: idx}
        
        # stopping condition-1
        while numerator != 0:
            numerator *= 10
            idx += 1
            fraction += str(numerator // denominator)
            numerator %= denominator 
            
            # stopping condition-2
            if numerator in memo:
                output = result + fraction[:memo[numerator]]
                output += '(' + fraction[memo[numerator]:] + ')'
                if sign == '-':
                    return '-' + output
                return output
            
            memo[numerator] = idx
            
        # handle negatives
        if sign == '-': return '-' + result + fraction
        return result + fraction


# January 12, 2023

'''

# Kunal Wadhwa

'''