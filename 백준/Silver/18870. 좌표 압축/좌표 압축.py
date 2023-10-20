import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
re_lst = lst[:]
lst.sort()
g = {}
cnt = 0

for i in lst:
    if i not in g:
        g[i] = cnt
        cnt += 1
for r in range(len(re_lst)):
    print(g[re_lst[r]], end=' ')
