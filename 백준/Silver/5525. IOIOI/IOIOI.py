import sys

n = int(sys.stdin.readline())

_len = int(sys.stdin.readline())

char = sys.stdin.readline().rstrip()

tchar = 'I' + 'OI' * n
tnum = n

ans = 0

s = 0
while len(char)-s >= n*2+1:
    if char[s] == 'I':
        e = s + 2
        cnt = 0
        while True:
            if e < len(char) and char[e-1]=='O' and char[e] == 'I':
                cnt += 1
                e += 2
            else:
                break
            if cnt == n:
                ans += 1
                cnt -= 1      
        s = e-1


    else:
        s += 1


print(ans)
