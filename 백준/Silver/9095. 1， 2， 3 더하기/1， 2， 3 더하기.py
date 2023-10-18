import sys
import collections

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())


def dfs(sum,target):
    if sum == target:
        return 1
    if sum > target:
        return 0
    return dfs(sum+1,target) + dfs(sum+2,target) + dfs(sum+3,target)


n = int(sys.stdin.readline())
for i in range(n):
    t = int(sys.stdin.readline())
    print(dfs(0, t))
    