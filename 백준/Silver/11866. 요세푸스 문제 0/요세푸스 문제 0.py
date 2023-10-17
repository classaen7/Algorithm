import sys
# import collections
# n, k = map(int, sys.stdin.readline().split())




n, k = map(int,sys.stdin.readline().split())

lst = list(range(1,n+1))

print('<', end = '')

idx = 0

for i in range(n-1):
    idx = (idx+k-1)%len(lst)
    print(lst[idx], end=", ")
    del lst[idx]
    
print(lst[0], end='')


print('>')