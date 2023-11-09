def solution(sequence, k):
    # 비내림차순 : 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우
    # 투포인터로 탐색
    s,e = 0,0
    re = []
    summ = sequence[0]
    
    # 합이 크면 : s+1 = summ - sequence[s]
    # 합이 작으면 : e+1 = summ + sequence[e]
    
    while s <= e < len(sequence):
        if summ == k:
            # print(s,e)
            if not re or re[1]-re[0] > e-s:
                re = [s,e]
            summ -= sequence[s]
            s += 1

        if summ < k:
            e += 1
            if e < len(sequence):
                summ += sequence[e]
            
        elif summ > k:
            summ -= sequence[s]
            s += 1

    return re
        
        
        
