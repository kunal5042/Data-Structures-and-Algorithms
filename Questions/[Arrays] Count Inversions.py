# Question: https://www.codingninjas.com/codestudio/problems/count-inversions_615?leftPanelTab=0
# Medium
# Similar to Reverse Pairs
from typing import Optional, List

from itertools import count
from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n) :
    def count_inversions(low, middle, high):
        cache = []
        pairs = 0
        right = middle + 1
        for idx in range(low, middle+1):
            while right <= high and arr[idx] > arr[right]:
                right += 1

            pairs += (right - (middle + 1))

        left, right = low, middle + 1
        while left <= middle and right <= high:
            if arr[left] < arr[right]:
                cache.append(arr[left])
                left += 1
            else:
                cache.append(arr[right])
                right += 1
        
        while left <= middle:
            cache.append(arr[left])
            left += 1

        while right <= high:
            cache.append(arr[right])
            right += 1

        for idx in reversed(range(low, high+1)):
            arr[idx] = cache.pop()

        return pairs
    
    def divide(low, high):
        if low >= high:
            return 0
        middle = (low + high) // 2
        pairs  = divide(low, middle)
        pairs += divide(middle+1, high)
        pairs += count_inversions(low, middle, high)
        return pairs
        
    return divide(0, len(arr)-1)

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))
# Question: https://www.codingninjas.com/codestudio/problems/count-inversions_615?leftPanelTab=0
# Medium
from typing import Optional, List

from itertools import count
from os import *
from sys import *
from collections import *
from math import *

def getInversions(arr, n) :
    def count_inversions(low, middle, high):
        cache = []
        pairs = 0
        right = middle + 1
        for idx in range(low, middle+1):
            while right <= high and arr[idx] > arr[right]:
                right += 1

            pairs += (right - (middle + 1))

        left, right = low, middle + 1
        while left <= middle and right <= high:
            if arr[left] < arr[right]:
                cache.append(arr[left])
                left += 1
            else:
                cache.append(arr[right])
                right += 1
        
        while left <= middle:
            cache.append(arr[left])
            left += 1

        while right <= high:
            cache.append(arr[right])
            right += 1

        for idx in reversed(range(low, high+1)):
            arr[idx] = cache.pop()

        return pairs
    
    def divide(low, high):
        if low >= high:
            return 0
        middle = (low + high) // 2
        pairs  = divide(low, middle)
        pairs += divide(middle+1, high)
        pairs += count_inversions(low, middle, high)
        return pairs
        
    return divide(0, len(arr)-1)

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))
'''

# Kunal Wadhwa

'''