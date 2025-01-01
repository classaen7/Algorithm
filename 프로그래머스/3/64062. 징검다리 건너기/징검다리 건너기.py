def solution(stones, k):
    def valid(length, target):
        s = -1
        for i in range(length):
            if stones[i]-target <= 0:
                if i-s>=k:
                    return False
            else:
                s = i
        return True
    
    length = len(stones)    
    
    s, e = min(stones)-1, max(stones)
    answer = 0
    
    while s <= e:  
        mid = (s+e) // 2
        
        if valid(length, mid):
            answer = max(answer, mid)
            s = mid + 1
        else:
            e = mid - 1
            
    return answer+1