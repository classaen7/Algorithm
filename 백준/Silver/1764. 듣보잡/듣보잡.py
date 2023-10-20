import sys
import collections

dic = collections.defaultdict(int)

n, m = map(int, sys.stdin.readline().split())
cnt = 0

for _ in range(n):
    name = sys.stdin.readline().rstrip()
    dic[name] += 1
for _ in range(m):
    name = sys.stdin.readline().rstrip()
    dic[name] += 1
    if dic[name] == 2:
        cnt += 1

print(cnt)
for i in sorted(dic.keys()):
    if dic[i]==2:
        print(i)


        


