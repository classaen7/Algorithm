import sys
import math
# A, B, C = map(int, sys.stdin.readline().split())

sys.setrecursionlimit(10**6)

def solve():
    N = int(input())
    
    import collections
    nodes = collections.defaultdict(list)

    for _ in range(N-1):
        n1, n2 = map(int, sys.stdin.readline().split())

        nodes[n1].append(n2)
        nodes[n2].append(n1)
    
    
    hist = [0]*(N+1)
    hist[1] = 1


    def dfs(lst, p_node):
        if hist[p_node] == 0:
            return
        for n in lst:
            if hist[n] == 0:
                hist[n] = p_node
                dfs(nodes[n], n)
            else:
                continue

    
    dfs(nodes[1], p_node=1)

    for p in hist[2:]:
        print(p)

# print(solve())
solve()

