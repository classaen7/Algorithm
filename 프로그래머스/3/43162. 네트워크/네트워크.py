def solution(n, computers):
    answer = 0
    
    net = [1] * n
    
    for i in range(n):
        if net[i]:
            answer += 1
            net[i] = 0
        
            deq = [i]
            while deq:
                node = deq.pop(0)
                
                for nxt in range(len(computers[node])):
                    if computers[node][nxt] == 1 and nxt != node and net[nxt]:
                        deq.append(nxt)
                        net[nxt] = 0
        
    
    
    return answer