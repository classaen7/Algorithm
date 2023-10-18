import sys
import collections

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())

def dfs(num):
    if virus[num] != 1:
        virus[num] = 1
        while g[num]:
            dfs(g[num].pop())

n = int(sys.stdin.readline())
virus = [0 for _ in range(n+1)]
m = int(sys.stdin.readline())

g = collections.defaultdict(list)
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    g[s].append(e)
    g[e].append(s)


dfs(1)
print(sum(virus)-1)