import sys

n, k = map(int, sys.stdin.readline().split())

mul, div =1, 1
    
for i in range(k):
    mul *= (n-i)
    div *= (k-i)
print(int(mul/div))