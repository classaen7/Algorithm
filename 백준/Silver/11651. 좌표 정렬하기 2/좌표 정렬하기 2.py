import sys

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())

n = int(sys.stdin.readline())

re = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    re.append([x,y])

re.sort(key=lambda x:(x[1],x[0]))
for r in re:
    print(r[0], r[1])