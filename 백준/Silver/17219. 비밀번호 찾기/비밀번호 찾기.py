import sys
import collections

psw = collections.defaultdict(str)

n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    site, pw = sys.stdin.readline().rstrip().split(' ')
    psw[site] = pw

for _ in range(m):
    print(psw[sys.stdin.readline().rstrip()])