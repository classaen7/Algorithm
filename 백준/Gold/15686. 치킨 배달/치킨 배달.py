import sys
import math
import collections

# A, B, C = map(int, sys.stdin.readline().split())

# sys.setrecursionlimit(10**6)

ans = [0]

def solve():
    N, M = map(int, sys.stdin.readline().split())   
    mtx = []

    chk = []
    for r in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        mtx.append(row)
        for c in range(N):
            if row[c] == 2:
                chk.append([r,c])
    

    hm = []

    for i in range(N):
        for j in range(N):
            if mtx[i][j] == 1:
                hm.append([i,j])
    
    def dist(x1,y1, x2,y2):
        return abs(x1-x2) + abs(y1-y2)


    import itertools
    combinations = list(itertools.combinations(range(len(chk)), M))
    
    import collections
    dic = collections.defaultdict(list)

    for h in range(len(hm)):
        for c in chk:
            dic[h].append(dist(hm[h][0],hm[h][1],c[0],c[1]))
    
    import math
    ans = math.inf

    for c in combinations:
        s = 0
        for h in range(len(hm)):
            tmp = math.inf
            for idx in c:
                tmp = min(tmp, dic[h][idx])
            s += tmp

        ans = min(s,ans)

    return ans


        

        
print(solve())
# solve()


