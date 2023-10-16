import sys


b_start = 'BWBWBWBW'
w_start = 'WBWBWBWB'

b_mtx = [b_start,w_start,b_start,w_start,b_start,w_start,b_start,w_start]
w_mtx = [w_start,b_start,w_start,b_start,w_start,b_start,w_start,b_start]

b_str = ''.join(b_mtx)
w_str = ''.join(w_mtx)


def check_min(n,m):
    b, w = 0, 0

    check_str = ""
    for i in range(8):
        for j in range(8):
            check_str = check_str + mtx[n+i][m+j]

    for i in range(64):
        if check_str[i] != b_str[i]:
            b += 1
        if check_str[i] != w_str[i]:
            w += 1
    
    return min(b,w)
    
N, M = map(int, input().split())

mtx = []

for i in range(N):
    mtx.append(list(sys.stdin.readline().rstrip()))


min_swap = sys.maxsize

for i in range(N-8+1):
    for j in range(M-8+1):
        min_swap = min(check_min(i,j), min_swap)

print(min_swap)


