def solution(n):
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    
    b = [[0] * n for _ in range(n)]
    x, y = -1, 0
    num = 1
    
    for i in range(n):
        for j in range(i, n):
            x += dx[i % 3]
            y += dy[i % 3]
            b[x][y] = num
            num += 1
            
    answer = [b[i][j] for i in range(n) for j in range(i+1) if b[i][j] != 0]
    return answer