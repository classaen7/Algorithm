import sys
import collections

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())

n = int(sys.stdin.readline())
mtx = []
ans = []

for _ in range(n):
    mtx.append(list(map(int,sys.stdin.readline().rstrip())))


def dfs(i,j):
    global n
    if 0 <= i < n and 0 <= j < n and mtx[i][j] == 1:
        mtx[i][j] = 0
        return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
    return 0

for i in range(n):
    for j in range(n):
        cnt = dfs(i,j)
        if cnt != 0:
            ans.append(cnt)
            
print(len(ans))
for i in sorted(ans):
    print(i)