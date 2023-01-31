# Question: https://leetcode.com/problems/lfu-cache/
# Hard
from typing import Optional, List
from collections import defaultdict
class DLLN:
    def __init__(self, value, frequency=0):
        self.val = value
        self.next = None
        self.prev = None
        self.freq = frequency

# SOLVED-1: TLE 65% test cases passed
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
        
# SOLVED-2: TLE 88% test cases passed
class LFUCache:

    def __init__(self, capacity: int):
        self.time = 0
        self.cache = {}
        self.capacity = capacity
        self.counter = defaultdict(int)

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.counter[key] += 1
        self.time += 1
        self.cache[key][1] = self.time
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        insertion, insertion_value = key, value
        if key in self.cache or len(self.cache) < self.capacity:
            self.time += 1
            self.cache[key] = [value, self.time]
            self.counter[key] += 1
            return
        
        least_fu = []
        min_freq = None
        for key, freq in self.counter.items():
            if min_freq is None:
                min_freq = freq
                least_fu.append(key)
                continue
            
            if freq < min_freq:
                min_freq = freq
                least_fu = [key]
                
            elif freq == min_freq:
                least_fu.append(key)
                
        if len(least_fu) == 1:
            discard = least_fu.pop()
            del self.cache[discard]
            del self.counter[discard]
        else:
            least_recent = None
            discard = None
            for key in least_fu:
                value, time = self.cache[key]
                if least_recent is None:
                    least_recent = time
                    discard = key
                
                if time < least_recent:
                    least_recent = time
                    discard = key
            del self.cache[discard]
            del self.counter[discard]
            
        self.time += 1
        self.counter[insertion] += 1
        self.cache[insertion] = [insertion_value, self.time]
        
# SOLVED-3: Accepted
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.frequencies = defaultdict(dict)

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        self.update(key)
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0: return
        if key in self.cache:
            self.update(key)
            self.cache[key][0] = value
            return
        
        if len(self.cache) < self.capacity:
            self.cache[key] = [value, 1]
            self.frequencies[1][key] = True
            return
        
        # remove the least frequenty used if there is not a tie
        min_freq = min(self.frequencies.keys())
        
        # no tie
        if len(self.frequencies[min_freq]) == 1:
            discard = list(self.frequencies[min_freq].keys())[0]
            del self.cache[discard]
            del self.frequencies[min_freq]
        else:
            # dict is ordered, so we are taking out the least recently inserted key
            for x in self.frequencies[min_freq]:
                discard = x
                break
                
            del self.cache[discard]
            del self.frequencies[min_freq][discard]
            
        # insert the new key, now that there is space
        self.cache[key] = [value, 1]
        self.frequencies[1][key] = True
        return
                
        
    def update(self, key):
        # remove from prev frequency hashmap
        del self.frequencies[self.cache[key][1]][key]
        
        # remove the record if empty
        if len(self.frequencies[self.cache[key][1]]) == 0:
            del self.frequencies[self.cache[key][1]]

        # add to new updated frequency hashmap
        self.frequencies[self.cache[key][1]+1][key] = True

        # increase frequency 
        self.cache[key][1] += 1


# January 29, 2023

'''

# Kunal Wadhwa

'''