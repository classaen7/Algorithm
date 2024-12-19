def solution(n):
    def count1(num):
        i = 0
        while num >0:
            if num %2 == 1:
                i += 1
            num = num//2
        return i
    
    target = n+1
    while True:
        if count1(n) == count1(target):
            break
        else:
            target += 1

    
    return target