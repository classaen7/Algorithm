import sys
# import collections

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())

def dfs(i,j):
    global n,m
    if 0 <= i <= m and 0 <= j <= n and mxt[i][j]:
        mxt[i][j] = 0
        return max(1, dfs(i-1,j), dfs(i+1,j), dfs(i,j-1),dfs(i,j+1))
    return 0

t = int(sys.stdin.readline())


for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    mxt = [ [0 for _ in range(m) ] for _ in range(n)]

    for _ in range(k):
        j, i = map(int, sys.stdin.readline().split())
        mxt[i][j] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if mxt[i][j] == 1:
                cnt += 1
                stack = [[i,j]]
                while stack:
                    r,c = stack.pop()
                    if 0 <= r < n and 0 <= c < m and mxt[r][c]:
                        mxt[r][c] = 0
                        stack.append([r-1,c])
                        stack.append([r+1,c])
                        stack.append([r,c-1])
                        stack.append([r,c+1])
                    


    print(cnt)
