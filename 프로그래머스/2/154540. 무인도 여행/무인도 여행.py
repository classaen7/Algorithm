import sys
 
def solution(maps):  
    limit_number = 10000
    sys.setrecursionlimit(limit_number)
        
    def dfs(i,j):
        # 종료조건
        if i < 0 or i >= len(maps) or j < 0 or j >= len(maps[0]) or maps[i][j] == 0:
            return 0
        
        temp, maps[i][j] = maps[i][j], 0
        
        return temp + dfs(i-1,j) + dfs(i,j-1) + dfs(i+1,j) + dfs(i, j+1)
        
        
    answer = []
    
    for i in range(len(maps)):
        maps[i] = [int(num) if num.isdigit() else 0 for num in maps[i]]
    
    
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            
            if maps[r][c] != 0:  #탐색 시작
                answer.append(dfs(r,c))

    return sorted(answer) if answer else [-1]