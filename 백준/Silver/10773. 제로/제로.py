import sys
import collections

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())



n = int(sys.stdin.readline())
stack = []
for i in range(n):
    t = int(sys.stdin.readline())
    if t == 0:
        stack.pop()
    else:
        stack.append(t)
print(sum(stack))
    