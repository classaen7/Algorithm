import math

def solution(r1, r2):
    answer = 0
    for x in range(0,r2+1):
        start_y = math.ceil((r1**2-x**2)**(1/2)) if x<=r1 else 0
        end_y = math.floor((r2**2-x**2)**(1/2))
        answer += end_y - start_y + 1
    answer *= 4
    answer -= (r2-r1+1)*4
    return answer