def solution(n, edge):
    lst = [[] for _ in range(n)]
    for n1, n2 in edge:
        lst[n1-1].append(n2-1)
        lst[n2-1].append(n1-1)
    
    deq = [0]
    
    visit = [0] * n
    visit[0] = 1
    
    while deq:
        last = len(deq)
        for i in range(len(deq)):
            next = deq.pop(0)
            
            for n in lst[next]:
                if not visit[n]:
                    visit[n] = 1
                    deq.append(n)
                        
        
    return last