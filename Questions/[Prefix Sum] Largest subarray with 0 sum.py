# Question: https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1
# Medium
# Good Edge-Cases
from typing import Optional, List

#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        last_seen  = {}
        prefix_sum = 0
        result = 0
        
        for idx in range(len(arr)):
            prefix_sum += arr[idx]
            
            # edge-case
            if arr[idx] == 0 and result == 0: result += 1
            
            # fact
            if prefix_sum == 0: result = idx + 1
            
            if prefix_sum in last_seen:
                result = max(result, idx - last_seen[prefix_sum])
            else:
                last_seen[prefix_sum] = idx
                
        return result


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
'''

# Kunal Wadhwa

'''