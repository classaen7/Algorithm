import sys
import collections

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())



n = int(sys.stdin.readline())

lst = [0]*1000000

for i in range(n):
    
    lst[int(sys.stdin.readline())] += 1

for i in range(len(lst)):
    if lst[i] != 0:
        for j in range(lst[i]):
            print(i)


