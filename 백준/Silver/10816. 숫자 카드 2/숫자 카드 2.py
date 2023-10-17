import sys
import collections
# n, k = map(int, sys.stdin.readline().split())


n = int(sys.stdin.readline())
cnt = collections.Counter(list(map(int,sys.stdin.readline().split())))
n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
re = []
for i in lst:
    re.append(str(cnt[i]))
print(' '.join(re))