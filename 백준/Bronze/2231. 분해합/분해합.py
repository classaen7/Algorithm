import sys

def divsum(num):
    for i in str(num):
        num += int(i)
    return num
n = int(sys.stdin.readline())

i = max(n - len(str(n))*9,0)

while True:
    if divsum(i) == n:
        print(i)
        break
    if i > n:
        print(0)
        break
    i += 1


