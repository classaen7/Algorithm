import sys
import collections

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())

n = int(sys.stdin.readline())

dp = {}
dp[0] = [1,0]
dp[1] = [0,1]
for i in range(2,41):
    dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]

for i in range(n):
    m = int(sys.stdin.readline())
    print(dp[m][0],dp[m][1],end=' ')



