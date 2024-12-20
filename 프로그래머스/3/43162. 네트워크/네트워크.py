def solution(n, computers):
    from collections import defaultdict
    answer = 0
    
    dic = defaultdict(list)
    for i in range(n):
        for idx, c in enumerate(computers[i]):
            if i != idx and c==1: 
                dic[i].append(idx)
                
    net = [1] * n

    for i in range(n):
        if net[i] == 1:
            answer += 1
            
            deq = [i]
            net[i] = 0
            
            while deq:
                node = deq.pop(0)
                for nxt in dic[node]:
                    if net[nxt] == 1:
                        net[nxt] = 0
                        deq.append(nxt)
    
    return answer