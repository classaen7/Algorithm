def solution(storey):
    answer = 0
    """
    4자리 vs 6자리 -> 1 => 5번
    """
    while storey>0:
        last_num = storey%10
        if last_num == 5:
            if storey > 10 and (storey//10) % 10 >= 5:
                storey += 5
                
            else:
                storey -= 5
            answer += 5
    
        elif last_num < 5:
            answer += last_num
            storey -= last_num
            storey = storey/10
        else:
            answer += (10-last_num)
            storey += (10-last_num)
            storey = storey/10
        
    return answer