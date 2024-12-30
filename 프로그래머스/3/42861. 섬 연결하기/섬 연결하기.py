def solution(n, costs):
    dist = [[float('Inf') if i!= j else 0 for i in range(n)] for j in range(n)]
    for n1, n2, w in costs:
        dist[n1][n2] = w
        dist[n2][n1] = w
    
    next = [i for i in dist[0]]
    answer = 0
    
    for _ in range(n-1):
        idx, min_value = -1, float('Inf')
        
        for i in range(len(next)):
            if next[i] != 0 and min_value > next[i]:
                min_value, idx = next[i], i
        
        answer += min_value
        
        for next_node in range(n):
            if next[next_node] > dist[idx][next_node] :
                next[next_node] = dist[idx][next_node]
                
        next[idx] = 0
            
    return answer