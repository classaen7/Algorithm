import sys
import collections

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())

n = int(sys.stdin.readline())


for i in range(n):
    n, m = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    length = len(lst)
    idx = 0

    for i, imp in enumerate(sorted(lst, reverse=True)): # 중요도 높은거 부터 방문 -> 동일한 것도 어차피 중요도만 보니까 ㄱㅊ
        
        while lst[idx]!=imp:
            idx = (idx+1)%length
        # print(f'{imp} : {idx}')

        if idx == m:
            print(i+1)
            break

        idx = (idx+1)%length



