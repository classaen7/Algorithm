from collections import deque

def solution(begin, target, words):
    
    visit = [begin]
    deq = deque([begin])
    dist = 0
    
    while deq:
        dist += 1
        
        for _ in range(len(deq)):
            node = deq.popleft()
            
            for w in words:
                if w not in visit and sum(1 for a,b in zip(node, w) if a!=b)==1:
                    if w == target:
                        return dist
                    visit.append(w)
                    deq.append(w)
        
    return 0
    
