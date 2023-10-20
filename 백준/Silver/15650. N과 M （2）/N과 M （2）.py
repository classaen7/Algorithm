import sys
import itertools

n, m = map(int, sys.stdin.readline().split())
lst = list(range(1,n+1))

for i in itertools.combinations(lst,m):
    print(*i)
