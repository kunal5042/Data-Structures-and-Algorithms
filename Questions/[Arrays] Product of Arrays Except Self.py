# Question: https://leetcode.com/problems/product-of-array-except-self/
# Medium
# Hard to solve in one pass and constant space. P.S: Done
class Solution:
    # O(n) Time and O(1) Space: where n is the length of the input array
    def productExceptSelf(self, nums):
        result = [1 for _ in range(len(nums))]
        
        # Logic: result[idx] = left_products[idx-1] * right_products[idx+1]
        # now, instead of storing left and right products in a separate array
        # we keep calculating them as we traverse the array simultaneously using them for resultant array calculation
        #
        # the products of all the left elements of index k will be used for resultant array calculation of index k+1
        # similarly, the products of right elements of index k will be used for resultant array calculation of index k -1
        #
        # using this idea, we maintain left and right product and update the k + 1 and w - 1 indices 
        # where, k is our current index of products from left
        # and w is our current index of products from right
        #
        
        # for better readability 
        last_idx = len(nums) - 1 
        
        # running products
        left_product    = 1
        right_product   = 1
        
        
        for idx in range(len(nums)):
            # k       = idx + 1
            # w       = last_idx - idx - 1
            
            
            # calculating running products
            left_product      *= nums[idx]
            right_product     *= nums[last_idx - idx]

            # updating the corresponding resultant indices
            if idx + 1 <= last_idx:
                result[idx + 1] *= left_product
                
            if last_idx - idx - 1 >= 0:
                result[last_idx - idx - 1]  *= right_product

                
        # result
        return result

# Kunal Wadhwa
