import sys

# A, B, C = map(int, sys.stdin.readline().split())

def solve():
    N = int(input())

    def func(num):
        num_lst = list(map(int,list(str(num))))
        bef = num_lst[0]
        diff = None
        num_lst = num_lst[1:]

        for i in num_lst:
            if diff is not None and diff != bef - i:
                return False
            diff = bef - i
            bef = i

        return True

    re = 0
    for i in range(1, N+1):
        if func(i):
            re += 1
    return re

    

print(solve())


