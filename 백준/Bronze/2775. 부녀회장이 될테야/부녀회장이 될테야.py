import sys
import collections

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())


c = int(sys.stdin.readline())

for i in range(c):
    k = int(sys.stdin.readline()) # 층
    n = int(sys.stdin.readline()) # 호

    lst = list(range(1,n+1))
    for i in range(k):
        sum = 0
        for i, p in enumerate(lst):
            sum += p
            lst[i] = sum

    print(lst[n-1])



