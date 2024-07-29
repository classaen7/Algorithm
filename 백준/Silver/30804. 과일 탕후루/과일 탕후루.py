import sys
import math
# A, B, C = map(int, sys.stdin.readline().split())

def solve():
    N = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))

    s = 0
    e_s, e_e = 0, 1

    re = 1

    seq = set([lst[s]])

    while e_e < len(lst):

        seq.add(lst[e_e])

        if len(seq) > 2:
            seq = set([lst[e_s], lst[e_e]])
            s = e_s
            e_s = e_e
        
        else:   
            re = max( re, e_e - s + 1)

            if lst[e_s] != lst[e_e]:
                e_s = e_e
            
        e_e += 1

    return re


print(solve())

