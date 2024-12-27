def solution(routes):
    answer = 0
    bef_s, bef_e = -30001, -30001
    
    for s,e in sorted(routes, key=lambda x:(x[0], -x[1])):
        if bef_s <= s <= bef_e:
            bef_s, bef_e = max(bef_s, s), min(bef_e, e)
            
        else:
            answer += 1
            bef_s, bef_e = s, e
    
    
        

    return answer