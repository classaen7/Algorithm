import sys



n, m = map(int, sys.stdin.readline().split())
sum = 0


lst = list(map(int, sys.stdin.readline().split()))
sum_lst = [0]
for x in lst:
    sum += x
    sum_lst.append(sum)

for _ in range(m):
    s,e = map(int, sys.stdin.readline().split())
    print(sum_lst[e]-sum_lst[s-1])
       
