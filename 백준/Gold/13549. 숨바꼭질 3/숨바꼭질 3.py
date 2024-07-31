import sys
import math
# A, B, C = map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10**6)

def solve():
    N, M = map(int, sys.stdin.readline().split())


    visited = [-1] * 100001
    def bfs():
        import collections
        deq = collections.deque([[N, 0]])
        visited[N] = 0

        while deq:
            x, t = deq.popleft()
            
            if 0<=x-1 and (visited[x-1] == -1 or visited[x-1] > t + 1):
                visited[x-1] = t+1
                deq.append([x-1,t+1])

            if x+1< 100001 and (visited[x+1] == -1 or visited[x+1] > t + 1):
                visited[x+1] = t+1
                deq.append([x+1,t+1])

            if x*2 < 100001 and (visited[x*2] == -1 or visited[x*2] > t):
                visited[x*2] = t
                deq.append([x*2,t])

        return visited[M]
    return bfs()


print(solve())
# solve()


