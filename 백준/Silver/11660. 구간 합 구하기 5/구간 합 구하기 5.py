import sys
import math
# A, B, C = map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10**6)

def solve():
    N, M = map(int, sys.stdin.readline().split())
    
    matrix = []
    for _ in range(N):
        row = list(map(int, sys.stdin.readline().split()))
        matrix.append(row)


    def func(i, j):
        if 0 <= i < N and 0 <= j < N:
            return matrix[i][j]
        return 0

    for i in range(N):
        for j in range(N):
            matrix[i][j] = matrix[i][j] + func(i-1,j) + func(i,j-1) - func(i-1, j-1)

    p = []

    for _ in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        # print(func(x2, y2))
        # print(func(x1-1, y1-1))
        # print(func(x2, y1-1))
        # print(func(x1-1,y2))
        p.append(func(x2, y2) + func(x1-1, y1-1) - func(x2, y1-1) -func(x1-1,y2))
            
    for i in p:
        print(i)

# print(solve())
solve()


