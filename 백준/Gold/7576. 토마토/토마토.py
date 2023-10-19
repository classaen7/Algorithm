import sys
import collections

m, n = map(int, sys.stdin.readline().split())

tomato = []
deq = collections.deque()

for r in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))
cnt = 0
for r in range(n):
    for c in range(m):
        if tomato[r][c]==1:
            deq.append([r,c])
        if tomato[r][c]==0:
            cnt += 1

move = [[1,0], [-1,0], [0,1], [0,-1]]

day = -1
while deq:
    for _ in range(len(deq)):
        r,c = deq.popleft()

        for ud,rl in move:
            nr, nc = r+ud, c+rl
            if 0 <= nr < n and 0 <= nc < m and tomato[nr][nc]==0:
                tomato[nr][nc] = 1
                cnt -= 1
                deq.append([nr,nc])
    day += 1

print(-1 if cnt!=0 else day)






