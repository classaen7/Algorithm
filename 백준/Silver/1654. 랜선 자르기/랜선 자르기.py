import sys

# n= sys.stdin.readline()

k, n = list(map(int, sys.stdin.readline().split()))

lst = []
for i in range(k):
    lst.append(int(input()))

left = 0
right = max(lst)*2

#
while True:
    div_len = (left+right)//2
    cnt = 0

    for i in lst:
        cnt += (i//div_len)
    
    if cnt < n: 
        left, right = left, div_len-1
    else: 
        max_len = div_len
        left, right = div_len+1, right

        while left<=right:
            mid = (left+right)//2
            cnt = 0
            for i in lst:
                cnt += (i//mid)
            
            if cnt < n:
                left, right = left, mid-1
            else:
                max_len = mid
                left, right = mid+1, right
        
        break

print(max_len)





