def solution(board):
    answer = 0
    
    ## 상하좌우
    
    # x = [0,0,-1,1]
    # y = [-1,1,0,0]
    
    x_len = len(board[0])
    y_len = len(board)
    

    start = (0,0)
    goal = (0,0)
    
    visit = {}
    
    for yy in range(y_len):
        for xx in range(x_len):
            t = board[yy][xx]
            if t != ".":
                if t == "G":
                    goal = (yy,xx)
                elif t == "R":
                    start = (yy,xx)
                    visit[start] = 1
    
    def go(y,x):
        temp_y = y
        temp_x = x
        temp = []
        ## 상
        while True:
            temp_y -= 1
            if temp_y == -1:
                temp_y += 1
                if board[temp_y][temp_x] == "G":
                    return False
                temp.append((temp_y,temp_x))
                break
            elif board[temp_y][temp_x] == "D":
                temp_y += 1
                if board[temp_y][temp_x] == "G":
                    return False
                temp.append((temp_y,temp_x))
                break
                    
        temp_y = y
        temp_x = x
        ## 하
        while True:
            temp_y += 1
            if temp_y == y_len:
                temp_y -= 1
                if board[temp_y][temp_x] == "G":
                    return False
                temp.append((temp_y,temp_x))
                break
            elif board[temp_y][temp_x] == "D":
                temp_y -= 1
                if board[temp_y][temp_x] == "G":
                    return False
                temp.append((temp_y,temp_x))
                break
        
        ## 좌
        temp_y = y
        temp_x = x
        while True:
            temp_x -= 1
            if temp_x == -1:
                temp_x += 1
                if board[temp_y][temp_x] == "G":
                    return False
                temp.append((temp_y,temp_x))
                break
            elif board[temp_y][temp_x] == "D":
                temp_x += 1
                if board[temp_y][temp_x] == "G":
                    return False
                temp.append((temp_y,temp_x))
                break
                    
        
        ## 우
        temp_y = y
        temp_x = x
        while True:
            temp_x += 1
            if temp_x == x_len:
                temp_x -= 1
                if board[temp_y][temp_x] == "G":
                    return False
                temp.append((temp_y,temp_x))
                break
            elif board[temp_y][temp_x] == "D":
                temp_x -= 1
                if board[temp_y][temp_x] == "G":
                    return False
                temp.append((temp_y,temp_x))
                break
    
    
        return temp
    li = [start]
    stack = 0
    while True:
        stack += 1
        temp = []
        for l in li:
            temp_go = go(*l)
            if temp_go:
                for g in temp_go:
                    if not visit.get(g):
                        temp.append(g)
                        visit[g] = 1
            else:
                return stack
            
        li = temp
        if not temp:
            return -1