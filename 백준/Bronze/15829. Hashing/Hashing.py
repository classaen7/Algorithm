import sys

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())


r = 31
m = 1234567891

n = int(sys.stdin.readline())
sum = 0
lst = list(sys.stdin.readline().rstrip())

for i in range(n):
    sum += (int(ord(lst[i]))-96) * (r**i)
print(sum%m)