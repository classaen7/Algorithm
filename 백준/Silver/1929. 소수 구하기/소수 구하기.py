import sys

M,N = list(map(int, sys.stdin.readline().split()))

tf = [True]*(N+1)
tf[0],tf[1] = False, False

for i in range(2,int(N**0.5)+1):
    if tf[i]==True:
        for j in range(i+i,N+1,i):
            tf[j] = False


for i, b in enumerate(tf[M:],M):
    if b == True:
        print(i)
