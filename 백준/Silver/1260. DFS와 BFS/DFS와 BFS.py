import sys
import collections

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())

dfs_visited = []

def dfs(node):
    if node not in dfs_visited:
        dfs_visited.append(node)
        for i in graph[node]:
            dfs(i)


n, m, v = map(int, sys.stdin.readline().split())

graph = collections.defaultdict(list)

for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

for n in graph:
    graph[n].sort()


dfs(v)
print(' '.join(map(str,dfs_visited)))



deq = collections.deque([v])
bfs_visited = [v]

while deq:
    node = deq.popleft()
    

    for i in graph[node]:
        if i not in bfs_visited:
            bfs_visited.append(i)
            deq.append(i)


print(' '.join(map(str,bfs_visited)))


