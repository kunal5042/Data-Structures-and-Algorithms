# Question: https://leetcode.com/problems/palindrome-linked-list/

from typing import Optional, List

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the middle node using slow and fast method
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        # reversing the right half
        current = slow
        previous = None
        while current != None:
            temp         = current.next
            current.next = previous
            previous     = current
            current      = temp
        
        # checking if the linked list is a palindrome
        # this will work for odd and even because
        #   - even: equally divided both halves, can be compared
        #   - odd : both the halves will point to the same node, so it won't be a problem 

        # and that is the reason we reversed the right half and not the left
        
        left = head
        right = previous
        
        while right != None:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
            
        return True
# Question: https://leetcode.com/problems/palindrome-linked-list/

class Solution:
    '''O(n) Time and O(1) Space'''
    def isPalindrome(self, head):
        # find the middle node using slow and fast method
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        # reversing the right half
        current = slow
        previous = None
        while current != None:
            temp         = current.next
            current.next = previous
            previous     = current
            current      = temp
        
        # checking if the linked list is a palindrome
        # this will work for odd and even because
        #   - even: equally divided both halves, can be compared
        #   - odd : both the halves will point to the same node, so it won't be a problem 

        # and that is the reason we reversed the right half and not the left
        
        left = head
        right = previous
        
        while right != None:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
            
        return True
    
    
    '''O(n) Time and O(1) Space'''
    # Longer code, same implementation as above
    def isPalindrome(self, head):
        # get the middle node
        previous, middle = self.get_middle(head)
        
        # find the lenght of the linked list
        len_list = self.get_length(head)
        
        # if length is 1, it's a palindrome
        if len_list == 1: return True
        
        # otherwise, reverse the right half and unlink both halves
        left_half, right_half = head, self.get_reversed_right_half(previous, middle, len_list)
        
        # compare both halves
        while left_half is not None and right_half is not None:
            if left_half.val != right_half.val:
                return False
            left_half = left_half.next
            right_half = right_half.next
            
        return True
       
    def reverse(self, node):
        previous = None
        
        while node is not None:
            temp = node.next
            node.next = previous
            previous = node
            node = temp
            
        return previous
    
    
    def get_length(self, node):
        len_list = 0
        current  = node
        while current is not None:
            len_list += 1
            current = current.next
            
        return len_list
    
    
    def get_reversed_right_half(self, previous, node, len_list):
        hare = node
        if len_list % 2 == 0:
            previous.next = None
            right_half = self.reverse(hare)
        else:
            previous.next = None
            right_half = self.reverse(hare.next)
            
        return right_half
    
    def get_middle(self, node):
        head = node
        hare, tortoise = head, head
        previous       = None
        
        while tortoise is not None and tortoise.next is not None:
            previous = hare
            hare     = hare.next
            tortoise = tortoise.next.next
            
        return previous, hare
    
# Kunal Wadhwa
'''

# Kunal Wadhwa


'''