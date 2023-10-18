import sys
import collections


# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())

n = int(sys.stdin.readline())

dp = [0]*1001
dp[1] = 1
dp[2] = 2
for i in range(3,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n]%10007)
