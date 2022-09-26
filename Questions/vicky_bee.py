from heapq import heapify, heappop, heappush
def uniq_sum(array, k):
    heap = [-ele for ele in array]
    heapify(heap)

    while k > 0 and len(heap) > 0:
        max_ele = heappop(heap)
        heappush(max_ele/2)
        heappush(max_ele/2)
        k -= 1

    answer = sum(set(heap))
    return -answer

print(uniq_sum())
