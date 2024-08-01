import sys
import math
import collections

# A, B, C = map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10**6)

def solve():
    N = int(input())
    M = int(input())
    
    # graph = collections.defaultdict(list)
    INF = math.inf

    mtx = [[INF if i!=j else 0 for i in range(N)] for j in range(N)]
    for _ in range(M):
        s, e, w = map(int, sys.stdin.readline().split())

        mtx[s-1][e-1] = min(mtx[s-1][e-1], w)
        # graph[s-1].append([e-1,w])


    for k in range(N):
        for i in range(N):
            for j in range(N):
                mtx[i][j] = min(mtx[i][j], mtx[i][k]+mtx[k][j])

    for i in mtx:
        for j in i:
            if j == INF:
                print(0, end=' ')
            else:
                print(j, end=' ')
        print()
    


    
# print(solve())
solve()


