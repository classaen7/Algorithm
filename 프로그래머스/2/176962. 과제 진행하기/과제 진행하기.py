import collections

def solution(plans):
    def time_to_min(time):
        h,m = map(int,time.split(':'))
        return h*60 + m
    
    ans = []
    
    plans.sort(key=lambda x:x[1])
    not_finish = []
    
    print(plans)
    
    for i in range(0,len(plans)-1):    
        
        
        fin_time = time_to_min(plans[i][1])+int(plans[i][2])
        # 뒤에거랑 비교
        left_time = time_to_min(plans[i+1][1]) - fin_time
        
        print(plans[i][0] , left_time)
        
        if left_time < 0: # 남는 시간 없을 때
            not_finish.append([plans[i][0],abs(left_time)])
        
        else:         #남는 시간 있을 때
            ans.append(plans[i][0])
            
            while not_finish and left_time>0:
                if left_time >= not_finish[-1][1]:
                    left_time -= not_finish[-1][1]
                    ans.append(not_finish.pop()[0])
                else:
                    not_finish[-1][1] -= left_time
                    break
                
                
                
    ans.append(plans[-1][0])     
    while not_finish:
        ans.append(not_finish.pop()[0])
    
    return ans
            
        
        
    
        
        
