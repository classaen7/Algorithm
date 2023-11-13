import heapq

def solution(picks, minerals):
    idx = {
        "diamond" : 0,
        "iron" : 1,
        "stone" : 2
    }
    pirodo = [[1, 1, 1],
              [5, 1, 1],
              [25, 5, 1]]
    
    if len(minerals) > sum(picks)*5:
        minerals = minerals[:sum(picks)*5]
    
    cnt = len(minerals)
    i = 0
    
    heap = []
    temp = [0,[]]
    
    while i < cnt:
        temp[0] += pirodo[2][idx[minerals[i]]]
        temp[1].append(minerals[i])
        i += 1
        
        if len(temp[1]) == 5:
            heapq.heappush(heap,(-temp[0],temp[1]))
            temp = [0,[]]
            
    if len(temp[1])>0:
        heapq.heappush(heap,(-temp[0],temp[1]))
    
    
    
    ans = 0
    for i in range(3):
        for j in range(picks[i]):

            if len(heap)==0:
                return ans
                
            _, mins = heapq.heappop(heap)

            for m in mins:
                ans += pirodo[i][idx[m]]
    return ans
            