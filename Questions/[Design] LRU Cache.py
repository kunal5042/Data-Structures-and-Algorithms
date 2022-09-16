# Question: https://leetcode.com/problems/lru-cache/
# Medium
from typing import Optional, List

class DLLN:
    def __init__(self, val):
        self.val  = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.cache = {}
        self.nodes = {}

    def get(self, key: int) -> int:
        # if not present
        if key not in self.cache:
            return -1
        
        # otherwise, update order
        return self.update_cache(key)
        
    def put(self, key: int, value: int) -> None:
        # empty cache, first insertion
        if self.head is None and self.tail is None:
            self.nodes[key] = DLLN(key)
            self.cache[key] = value
            self.head = self.nodes[key]
            self.tail = self.nodes[key]
            return
            
        # capacity not full, insert at the end
        if len(self.cache) < self.capacity and key not in self.cache:
            self.cache[key] = value
            self.nodes[key] = DLLN(key)
            self.tail.next  = self.nodes[key]
            self.nodes[key].prev = self.tail
            self.tail = self.tail.next
            self.tail.next = None
            return
        
        # evict Least-Recently-Used
        if len(self.cache) == self.capacity and key not in self.cache:
            # special case
            if self.capacity == 1:
                del self.nodes[self.head.val]
                del self.cache[self.head.val]
                self.nodes[key] = DLLN(key)
                self.cache[key] = value
                self.head = self.nodes[key]
                self.tail = self.nodes[key]
                return
            
            # remove from the front
            del self.cache[self.head.val]
            del self.nodes[self.head.val]
            
            # update front
            self.head.next.prev = None
            self.head = self.head.next
            
            # insert at the end
            self.nodes[key] = DLLN(key)
            self.cache[key] = value
            self.tail.next = self.nodes[key]
            self.nodes[key].prev = self.tail
            
            # udpate end
            self.tail = self.nodes[key]
            self.tail.next = None
            return
        
        # updation required instead of insertion
        self.cache[key] = value
        self.update_cache(key)
    
    def update_cache(self, recently_used_key):
        key = recently_used_key
        node = self.nodes[key]
        
        # single-node, no updation required
        if node.prev is None and node.next is None:
            return self.cache[key]
        
        # more than one node
        # and the node to be updated is head
        if node.prev is None:
            self.head = node.next
            node.next.prev = None
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None
            return self.cache[key]
            
        # more than one node
        # and the node to be updated is tail
        if node.next is None:
            return self.cache[key]
        
        # more than two nodes
        
        # disconnect
        node.prev.next = node.next
        node.next.prev = node.prev
        
        # insert at the end
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        self.tail.next = None
        
        return self.cache[key]
'''

# Kunal Wadhwa

'''

class DLLN:
    def __init__(self, value, frequency=0):
        self.val = value
        self.next = None
        self.prev = None
        self.freq = frequency
        
class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.nodes = {}
        self.capacity = capacity
        self.head = DLLN(-1, float('-inf'))
        self.tail = DLLN(-1, float('inf'))
        self.tail.prev = self.head
        self.head.next = self.tail
        
    def traverse(self):
        current = self.head
        while current is not None:
            if current.val != -1:
                print(current.val, ':', self.cache[current.val], end=',  ')
            else:
                print(current.val, ': +-inf', end=',  ')

            current = current.next
        print()

    def get(self, key: int) -> int:
        # self.traverse()
        if key not in self.cache:
            return -1
        
        self.update(key)
        return self.cache[key]
    
    def update(self, key):
        node = self.nodes[key]
        node.freq += 1
        
        while node.freq >= node.next.freq:
            previous_node = node.prev
            next_node = node.next
            
            previous_node.next = next_node
            next_node.prev = previous_node
            
            node.next = next_node.next
            next_node.next = node
            node.prev = next_node

    def put(self, key: int, value: int) -> None:
        # print(f'traverse for {key} and {value}')
        # self.traverse()
        if key in self.cache:
            self.cache[key] = value
            self.update(key)
            return
        
        self.nodes[key] = DLLN(key)
        
        if len(self.cache) < self.capacity:
            self.cache[key] = value
            self.insert_node(key)
            return

        # capacity-full
        if self.capacity == 0:
            return
        
        invalidated_key = self.head.next.val
        del self.cache[invalidated_key]
        del self.nodes[invalidated_key]
        
        invalidated_node = self.head.next
        self.head.next = invalidated_node.next
        invalidated_node.prev = self.head
        
        self.cache[key] = value
        self.insert_node(key)
        
    def insert_node(self, key):
        previous_node  = self.head
        next_node = self.head.next

        previous_node.next = self.nodes[key]
        self.nodes[key].prev = previous_node

        self.nodes[key].next = next_node
        next_node.prev = self.nodes[key]

        self.update(key)
        
        
        
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)