import collections

"""
dp = 연산 횟수를 저장

x가 최소임은 자명함 = 0

"""
def solution(x, y, n):
    answer = 0
    
    dp = collections.defaultdict(int)
    cand = collections.deque([x])
    
    while cand:
        
        for _ in range(len(cand)):
            num = cand.popleft() # 확인하려는 숫자
            if num == y:
                return dp[num]
            
            
            if dp[num+n] == 0 and num + n <= y:
                dp[num+n] = dp[num] + 1
                cand.append(num+n)
            
            if dp[num*2] == 0 and num * 2 <= y:
                dp[num*2] = dp[num] + 1
                cand.append(num*2)
            
            if dp[num*3] == 0 and num * 3 <= y:
                dp[num*3] = dp[num] + 1
                cand.append(num*3)
                
            # if dp[num*6] == 0 and num * 6 <= y:
            #     dp[num*6] = dp[num] + 2
            #     cand.append(num*6)
                
        
    return -1
    
    