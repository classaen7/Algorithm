import heapq

def solution(n, works):
    heap = []
    for w in works:
        heapq.heappush(heap, -w)
    
    for _ in range(n):  
        x = heapq.heappop(heap) + 1
        
        if x != 0:
            heapq.heappush(heap, x)
        
        if len(heap)==0:
            return 0
    
    answer = 0

    for h in heap:
        answer += h**2
    
    return answer