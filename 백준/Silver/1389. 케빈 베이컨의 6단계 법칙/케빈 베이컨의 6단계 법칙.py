import sys
import math
# A, B, C = map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10**6)

def solve():
    N, M = map(int, sys.stdin.readline().split())

    import collections
    graph = collections.defaultdict(list)

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    def bfs(s):
        re = [-1] * (N+1)
        
        deq = collections.deque([s])

        while deq:
            node = deq.popleft()

            for n in graph[node]:
                if re[n] == -1:
                    re[n] = re[node] + 1
                    deq.append(n)

        return sum(re)



    ans = []
    for i in range(1, N+1):
        ans.append(bfs(i))
    

    return ans.index(min(ans))+1

    
print(solve())
# solve()


