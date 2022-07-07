# Question: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class Solution:
    def deleteDuplicates(self, head):
        if head is None: return head
        
        previous = head
        current  = head.next
        
        while current is not None:
            if current.val == previous.val:
                # found duplicate, scan further
                while current.val == previous.val:
                    current = current.next
                    if current is None:
                        break
                    
                previous.next = current
                previous = current
                if current is not None:
                    current  = current.next
            else:
                previous = current
                current = current.next
        
        return head
# Kunal Wadhwa