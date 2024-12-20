def solution(triangle):
    for i in range(1, len(triangle)):
        for idx in range(len(triangle[i])):
            add_n = 0
            if idx-1 >= 0:
                add_n = max(add_n, triangle[i-1][idx-1])
            if idx < len(triangle[i-1]):
                add_n = max(add_n, triangle[i-1][idx])
            
            triangle[i][idx] += add_n
                
    return max(triangle[-1])