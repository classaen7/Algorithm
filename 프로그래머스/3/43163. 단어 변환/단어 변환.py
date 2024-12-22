def solution(begin, target, words):
    idx = -1
    for i in range(len(words)):
        if words[i] == target:
            idx = i
            break
    if idx== -1:
        return 0    
    
    lst = [begin] + words 
    
    dist = [[float('Inf') for _ in lst] for _ in lst]
    
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i==j:
                dist[i][j] = 0
            elif sum(1 for a,b in zip(lst[i], lst[j]) if a!=b) == 1:
                dist[i][j] = 1
                
    
    for k in range(len(lst)):
        for i in range(len(lst)):
            for j in range(len(lst)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j] 
    
    return 0 if dist[0][idx+1] == float('Inf') else dist[0][idx+1]
    
