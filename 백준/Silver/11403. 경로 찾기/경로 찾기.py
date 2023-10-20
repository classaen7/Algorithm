import sys

def dfs(node):
    for idx,n in enumerate(mtx[node]):        
        if n == 1 and visited[idx]==0:
            visited[idx] = 1
            dfs(idx)

n = int(sys.stdin.readline())
mtx = []

for _ in range(n):
    mtx.append(list(map(int, sys.stdin.readline().split())))

# 인덱스는 0부터 n-1 노드로
for i in range(n):
    visited = [0 for _ in range(n)]
    dfs(i)
    mtx[i] = visited

for i in mtx:
    print(*i)