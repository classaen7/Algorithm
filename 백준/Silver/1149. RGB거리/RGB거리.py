import sys

n = int(sys.stdin.readline())

mtx = []
for _ in range(n):
    mtx.append(list(map(int, sys.stdin.readline().split())))

dp = [[0,0,0] for _ in range(n)]
dp[0] = mtx[0]


for i in range(1,n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + mtx[i][0]
        elif j == 1:
            dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + mtx[i][1]
        else: # j==2
            dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + mtx[i][2]

print(min(dp[n-1]))
        