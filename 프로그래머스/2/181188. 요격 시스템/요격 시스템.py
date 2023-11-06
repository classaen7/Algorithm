import collections 

def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))
    deq_t = collections.deque(targets)
    ans = 0

    while deq_t:
        ans += 1
        _,e = deq_t.popleft()
        
        while deq_t and e > deq_t[0][0]:
            deq_t.popleft()
        
    return ans