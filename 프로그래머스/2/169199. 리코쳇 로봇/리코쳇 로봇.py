import collections

def solution(board):
    
    answer = -1
    move = [ [1,0], [-1,0], [0,1], [0,-1] ]
    dp = [ [0 for _ in range(len(board[0]))] for _ in range(len(board))]
    
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                pos = [i,j]

    deq = collections.deque([pos])
    dp[pos[0]][pos[1]] = 1
    
    while deq:
        answer += 1
        for _ in range(len(deq)):
            p = deq.popleft()
            if board[p[0]][p[1]] == 'G':
                return answer
            for i,j in move:
                n,m = p[0], p[1]
                while 0<=n+i<len(board) and 0<=m+j<len(board[0]) and board[n+i][m+j]!='D':
                    n,m = n+i, m+j
                if dp[n][m] == 0:
                    deq.append([n,m])
                    dp[n][m] = 1
                

    return -1
