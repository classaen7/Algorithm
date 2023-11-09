def solution(sequence, k):
    # 비내림차순 : 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우
    # 투포인터로 탐색 : 부분합
    
    s,e = 0,0
    re = []                                     # 정답 후보를 저장
    summ = sequence[0]
    
    # 합이 크면 : s+1 = summ - sequence[s]
    # 합이 작으면 : e+1 = summ + sequence[e]
    
    while e < len(sequence):
        if summ == k:                           # 투포인터의 부분합 확인
            if not re or re[1]-re[0] > e-s:     # 정답 후보와 비교 (길이가 더 짧은지, 시작점에 대한 비교는 불필요)
                re = [s,e]                      # 갱신
            summ -= sequence[s]
            s += 1
        
        # 부분합이 k와 다른경우 
        if summ < k:                        
            e += 1
            if e < len(sequence):
                summ += sequence[e]
            
        elif summ > k:
            summ -= sequence[s]
            s += 1

    return re
        
        
        
