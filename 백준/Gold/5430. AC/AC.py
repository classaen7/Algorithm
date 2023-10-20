import sys
import collections

def command_print(cmd, deq):
    if len(deq) < cmd.count('D'):
        print("error")
        return

    front = 1
    for c in cmd:
        if c == 'R':
            front *= -1

        else: # c == 'D'
            if front==1:
                deq.popleft()
            else:
                deq.pop()

    if front == -1:
        deq.reverse()

    print('[',end='')
    print(*deq,sep=',',end='')
    print(']')
    return


t = int(sys.stdin.readline())
for _ in range(t):
    cmd = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    lst = sys.stdin.readline().rstrip()
    lst = lst[1:len(lst)-1]
    if len(lst)==0:
        command_print(cmd,[])
    else:
        deq = collections.deque(list(map(int,lst.split(','))))
        command_print(cmd,deq)
    
  
 