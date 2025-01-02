def solution(lst):
    def is_palindrome(s, e):
        for i in range((e-s)//2+1):
            if lst[s+i] != lst[e-i]:
                return False
        return True
        
    
    dp = [[0 for _ in range(len(lst))]for _ in range(len(lst))]
    
    from collections import deque
    s, e = 0, len(lst)-1
    
    deq = deque([[s,e]])
    max_seq = -1
    
    while deq:
        deq_s, deq_e = deq.popleft()
        
        if is_palindrome(deq_s, deq_e):
            max_seq = max(max_seq, deq_e-deq_s+1)
        else:
            if dp[deq_s+1][deq_e] == 0:
                dp[deq_s+1][deq_e] = 1
                deq.append([deq_s+1, deq_e])
            
            if dp[deq_s][deq_e-1] == 0:
                dp[deq_s][deq_e-1] = 1
                deq.append([deq_s, deq_e-1])
            
            if dp[deq_s+1][deq_e-1] == 0:
                dp[deq_s+1][deq_e-1] = 1
                deq.append([deq_s+1, deq_e-1])
            
    
    return max_seq
        
    
    
    
    
