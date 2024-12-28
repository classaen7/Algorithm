import math
def solution(n, stations, w):
    def calc(s, e):
        return math.ceil((e-s+1)/(w*2+1)) if s <= e else 0
    
    answer =0 
    bef = 1
    for st in stations:
        answer += calc(bef, st-w-1)
        bef = st+w + 1
    answer += calc(bef, n)
    return answer