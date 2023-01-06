import heapq
def solution(numbers):
    
    maxheap = []
    for i in numbers:
        heapq.heappush(maxheap, - i)
    
    heapq.heapify(numbers)
    minheap = numbers
    a = heapq.heappop(maxheap) * heapq.heappop(maxheap)
    b = heapq.heappop(minheap) * heapq.heappop(minheap)
    
    if a >= b:
        return a
    else:
        return b
