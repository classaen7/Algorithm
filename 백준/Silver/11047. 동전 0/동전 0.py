import sys
import collections
import time
# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())


n, k = map(int, sys.stdin.readline().split())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))

cnt = 0

for i in range(len(lst)-1,-1,-1):
    cnt += k//lst[i]
    k = k - (k//lst[i])*lst[i]

print(cnt)