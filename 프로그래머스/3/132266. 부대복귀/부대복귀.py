def solution(n, roads, sources, destination):
    answer = [-1] * n
    answer[destination-1] = 0
    
    from collections import defaultdict
    dic = defaultdict(list)
    for n1, n2 in roads:
        dic[n1-1].append(n2-1)
        dic[n2-1].append(n1-1)
        
    
    deq = [destination-1]
    cnt = 1
    
    while deq:
        
        for i in range(len(deq)):
            node = deq.pop(0)
            
            for next in dic[node]:
                if answer[next] == -1:
                    answer[next] = cnt
                    deq.append(next)
            
        
        cnt += 1
    
    temp = []
    for s in sources:
        temp.append(answer[s-1])
        
    return temp 