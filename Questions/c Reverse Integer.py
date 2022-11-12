# Question: https://leetcode.com/problems/reverse-integer/
# Medium
from typing import Optional, List

class Solution {
public:
    // O(log(x)) Time and O(1) Space
    int reverse(int x) {
        int reverse = 0;
        while (x != 0){
            int pop = x % 10;
            x /= 10;
            // The interviewer wants to see if you check for integer overflow or not
            // That's the only reason this question is asked
            // Python3 doesn't have integer overflows
            if(reverse > INT_MAX/10 || (reverse == INT_MAX/10 && pop > 7)) return 0;
            if(reverse < INT_MIN/10 || (reverse == INT_MIN/10 && pop < -8)) return 0;
            reverse = reverse * 10 + pop;
        }
        return reverse;
    }
};
'''

# Kunal Wadhwa

'''