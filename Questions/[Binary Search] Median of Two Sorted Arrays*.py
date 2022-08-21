# Question: https://leetcode.com/problems/median-of-two-sorted-arrays/
# Hard
# Constraint: Time complexity should be O(log(m+n))

class Solution:
    # Time: log(min(n, m))
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B   = nums1, nums2
        total  = len(nums1) + len(nums2)
        half   = total // 2
        
        if len(B) < len(A):
            A, B = B, A
        
        left, right = 0, len(A) - 1
        
        while True:
            idx  = (left + right) // 2 # A
            jdx  = half - idx - 2 # B
        
            Aleft  = A[idx]         if idx >= 0             else float("-infinity")
            Aright = A[idx + 1]     if (idx + 1) < len(A)   else float("infinity")
            Bleft  = B[jdx]         if jdx >= 0             else float("-infinity")
            Bright = B[jdx+ 1]      if (jdx + 1) < len(B)   else float("infinity")
        
            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright:
                right = idx - 1
                
            else:
                left = idx + 1
                
# Kunal Wadhwa