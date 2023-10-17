import sys

A, B, V = map(int,sys.stdin.readline().split())



n = (V-A) // (A-B)
l = (V-A) % (A-B)

if l != 0:
    V -= n * (A-B)
    while V > 0:
        n += 1
        V -= A
        if V <=0 :
            print(n)
            break
        V += B

else:
    print(n+1)