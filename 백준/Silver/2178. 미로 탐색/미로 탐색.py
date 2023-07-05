from collections import deque

len_y,len_x = map(int, input().split())

array = [list(map(int,input())) for i in range(len_y)]

## 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def BFS(y,x):
    queue = deque()
    queue.append((y,x))
    while queue:
        y,x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0<=ny<len_y and 0<=nx<len_x and array[ny][nx] == 1:
                array[ny][nx] = array[y][x] + 1
                queue.append((ny,nx))
                
    return array[len_y-1][len_x-1]

print(BFS(0,0))
         
        
        
        