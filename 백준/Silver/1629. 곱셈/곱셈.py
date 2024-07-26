import sys


def solve():
    A, B, C = map(int, sys.stdin.readline().split())

    def func(b):
        if b == 1:
            return A % C
        if b % 2 == 1:
            return func(1) * func(b-1) % C

        return (func(b/2) ** 2) % C
    
    return func(B)


print(solve())

