import collections

def solution(plans):
    def time_to_min(time):                  # 시간을 비교,계산하기 위한 함수
        h,m = map(int,time.split(':'))
        return h*60 + m
    
    ans = []
    plans.sort(key=lambda x:x[1])
    not_finish = []

    for i in range(0,len(plans)-1):    
        
        fin_time = time_to_min(plans[i][1])+int(plans[i][2])    #i번째 공부가 끝나는 시간 계산
        left_time = time_to_min(plans[i+1][1]) - fin_time       #i+1 번째 공부와 비교하여 남는시간 계산
        
        
        if left_time < 0:                                       # 남는 시간 없을 때
            not_finish.append([plans[i][0],abs(left_time)])     # 끝내지 못한 과제로 ["이름",시간] 저장
        
        else:                                                   #남는 시간 있을 때
            ans.append(plans[i][0])
            
            while not_finish and left_time>0:                   #못끝낸 과제 하기
                if left_time >= not_finish[-1][1]:              #시간 충분
                    left_time -= not_finish[-1][1]
                    ans.append(not_finish.pop()[0])
                else:                                           #시간 부족
                    not_finish[-1][1] -= left_time
                    break
   
    ans.append(plans[-1][0])                                    #마지막건 바로
    
    while not_finish:                                           #스택 남아있으면 넣기
        ans.append(not_finish.pop()[0])
    
    return ans
            
        
        
    
        
        
