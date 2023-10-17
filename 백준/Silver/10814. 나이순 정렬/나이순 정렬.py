import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    info = sys.stdin.readline().rstrip().split(' ')
    lst.append([int(info[0]), info[1]])
for j in sorted(lst, key=lambda x:x[0]):
    print(j[0], j[1])
