import sys
import collections

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

cnt = collections.Counter(lst)

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

for i in lst:
    if cnt[i] != 0:
        print(1)
    else:
        print(0)