import sys
import math
# A, B, C = map(int, sys.stdin.readline().split())

def solve():
    N = int(input())
    size = list(map(int, sys.stdin.readline().split()))
    
    T, P = map(int, sys.stdin.readline().split())

    re_t = 0
    for s in size:
        re_t += math.ceil(s/T)
    
    print(re_t)

    print(N // P, N % P )


    


solve()


