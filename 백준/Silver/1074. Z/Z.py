import sys

n,r,c = map(int, sys.stdin.readline().split())

bin_size = [2**N for N in range(n,0,-1)]

start_row, start_col = 0, 0

rank = 0
for s in bin_size:
    mid_row, mid_col = start_row+ s//2, start_col+ s//2

    if r == mid_row and c == mid_col:
        rank += (s*s)//4*3
        break
    
    
    if r < mid_row and c < mid_col:
        rank += (s*s)//4*0

    elif r < mid_row and c >= mid_col:
        start_col = mid_col
        rank += (s*s)//4*1
    
    elif r >= mid_row and c < mid_col:
        start_row = mid_row
        rank += (s*s)//4*2
    
    elif r >= mid_row and c >= mid_col:
        start_row, start_col = mid_row, mid_col
        rank += (s*s)//4*3
    
print(rank)



