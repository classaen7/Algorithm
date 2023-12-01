"""
    시간복잡도
    4^7*100 = 1,638,400
"""

def solution(users, emoticons):
    def dfs(d_rates):
        if len(d_rates) == len(emoticons):
            discount.append(d_rates)
            return
        
        for i in discount_rate:
            dfs(d_rates+[i])

    answer = []
    discount_rate = [10,20,30,40]
    

    # 할인율의 조합 만들기 - 이모티콘의 길이 만큼 중첩 반복해야 함 -> 그래프 탐색
    discount = []
    dfs([])
    
    
    for d in discount:
        
        # d : 각 이모티콘의 할인율
        price, prem = 0, 0
        
        for u in users:
            u_price = 0
            for i in range(len(d)):
                if d[i] >= u[0]:
                    u_price += int(emoticons[i]*(100-d[i])//100)
            
            if u_price >= u[1]:
                prem += 1
            else:
                price += u_price
        answer.append([prem,price])

    answer.sort()
    return answer[-1]