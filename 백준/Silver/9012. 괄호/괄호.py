import sys

def isps(char):
    stack = []
    for i in char:
        if i == '(':
            stack.append('(')
        else:
            if len(stack) > 0:
                stack.pop()

            else:
                return False
    return len(stack) == 0


n = int(input())

lst = []

for i in range(n):
    ps = sys.stdin.readline().rstrip()
    lst.append(ps)


for i in lst:
    if isps(i):
        print("YES")
    else:
        print("NO")

    

