import sys

target = int(sys.stdin.readline())

n = int(sys.stdin.readline())
banned = list(map(int, sys.stdin.readline().split()))

lst = [1000000]*1000001

for i in range(1000001):
    if any(int(n) in banned for n in str(i) ):
        continue
    else:
        lst[i] = abs(target-i) + len(str(i))
lst[100] = abs(target-100)


print(min(lst))
