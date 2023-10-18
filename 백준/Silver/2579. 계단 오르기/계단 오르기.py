import sys

def sol():
    n = int(sys.stdin.readline())
    h = []
    dp = [[0,0] for _ in range(n)]

    for _ in range(n):
        h.append(int(sys.stdin.readline()))

    if n<=2:
        print(sum(h))
        return

    dp[0] = [h[0],h[0]]
    dp[1] = [h[0]+h[1],h[1]]

    for i in range(2,n):
        dp[i] = [dp[i-1][1]+h[i] ,max(dp[i-2])+h[i]] 


    print(max(dp[n-1]))
    return

sol()


