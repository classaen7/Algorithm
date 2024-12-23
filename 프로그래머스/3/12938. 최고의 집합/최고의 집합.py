def solution(n, s):
    if s // n == 0:
        return [-1]
    
    if s % n == 0:
        return [s//n] * n
    
    re = [s//n] * n
    
    for i in range(s%n):
        re[n-1-i] += 1
    return re
    
    

    