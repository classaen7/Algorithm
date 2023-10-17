import sys

N, M = map(int,sys.stdin.readline().split())

lst = list(map(int,sys.stdin.readline().split()))

lst.sort()
flag = 0

re, abs_num = 0, sys.maxsize

for i in range(len(lst)-2):
    if flag == 1:
        break
    target = M - lst[i]
    left, right = i+1, len(lst)-1

    while left < right:
        sum = lst[left] + lst[right]
        if sum > target:
            right -= 1
        
        elif sum < target:
            if abs_num > M - (sum+lst[i]):
                abs_num = M - (sum+lst[i])
                re = sum + lst[i]
            left += 1
        else:
            print(M)
            flag = 1
            break

if flag == 0:
    print(re)
        
