import sys

# n, k = map(int, sys.stdin.readline().split())
# n = int(sys.stdin.readline())

def is_bal(w):
    stack = []
    for i in w:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')' or i ==']':
            if len(stack) > 0:
                c = stack.pop()
                if (c=='(' and i ==')') or (c=='[' and i ==']'):
                    continue
                else:
                    return "no"
            else:
                return "no"
    
    return "yes" if len(stack) == 0 else "no"

while True:
    w = sys.stdin.readline().rstrip()
    if w =='.':
        break
    print(is_bal(w))

    
