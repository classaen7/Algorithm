import sys
import collections

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(list(map(int,sys.stdin.readline().split())))
for j in sorted(lst, key=lambda x:(x[0],x[1])):
    print(j[0], j[1])
