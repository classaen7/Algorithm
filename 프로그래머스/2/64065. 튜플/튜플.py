def solution(s):
    lst = []
    
    for i in s[1:-2].split('},'):
        temp = list(map(int,i[1:].split(',')))
        lst.append(temp)
    lst.sort(key=lambda x:len(x))
    
    answer = lst[0]
    
    b = set(answer)
    
    for l in lst[1:]:
        s = set(l)
        answer.append((s-b).pop())
        b = set(l)
    
    return answer