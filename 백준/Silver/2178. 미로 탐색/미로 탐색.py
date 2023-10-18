import sys
import collections

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())


n, m = map(int, sys.stdin.readline().split())
lst = []
dp = [[0 for j in range(m)] for i in range(n)]


for i in range(n):
    lst.extend(list(sys.stdin.readline().split()))

deq = collections.deque([[0,0]])
step = 0
while deq:

    step += 1
    for _ in range(len(deq)):
        i,j = deq.popleft()
        if i < 0 or j < 0 or i>=n or j>=m or lst[i][j] == '0' or dp[i][j] != 0:
           continue

        dp[i][j] = step

        deq.append([i,j+1])
        deq.append([i,j-1])
        deq.append([i-1,j])
        deq.append([i+1,j])



    
print(dp[n-1][m-1])
