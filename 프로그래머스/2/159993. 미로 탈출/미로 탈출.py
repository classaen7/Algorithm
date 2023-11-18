import collections

def solution(maps):
    """
    시작을 레버에서 시작
    레버 부터 Start까지 : ltos
    레버 부터 EXIT까지 : ltoe
    """
    move = [[1,0], [-1,0], [0,1], [0,-1]]
    
    visited = [ [0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'L':
                visited[i][j] = 1
                deq = collections.deque([[i,j]])

    ltos, ltoe = 0, 0  
    step = 0

    while deq:
        step += 1
        for _ in range(len(deq)):
            r,c = deq.popleft()
            print(r,c)
            for n,m in move:
                new_r, new_c = r+n, c+m
                if 0 <= new_r < len(maps) and 0 <= new_c < len(maps[0]) and visited[new_r][new_c]==0 and maps[new_r][new_c]!='X':
                    visited[new_r][new_c] = 1
                    
                    if maps[new_r][new_c] == 'S':
                        ltos = step    
                    elif maps[new_r][new_c] == 'E':
                        print(step)
                        ltoe = step
                        
                    deq.append([new_r, new_c])

    return ltos + ltoe if ltos!=0 and ltoe!= 0 else -1