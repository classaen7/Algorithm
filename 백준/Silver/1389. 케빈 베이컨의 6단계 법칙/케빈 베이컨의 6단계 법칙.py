import sys
import math
# A, B, C = map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10**6)

def solve():
    N, M = map(int, sys.stdin.readline().split())

    
    mtx = [[5001 if i!=j else 0 for j in range(N+1)] for i in range(N+1)]

    

    for _ in range(M):
        i, j = map(int, sys.stdin.readline().split())
        mtx[i][j] = 1
        mtx[j][i] = 1


    for k in range(1,N+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                mtx[i][j] = min(mtx[i][j], mtx[i][k]+ mtx[k][j])

    score = []
    for i in range(1,N+1):
        score.append([i, sum(mtx[i][1:])])
    
    score.sort(key=lambda x: (x[1],x[0]))
    return score[0][0]
    




print(solve())
# solve()


