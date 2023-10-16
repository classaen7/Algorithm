import sys
# import collections
# n, k = map(int, sys.stdin.readline().split())




n= int(sys.stdin.readline())

check = 1
re = 1
while True:
    if check >= n:
        print(re)
        break
    check +=  re*6
    re += 1



