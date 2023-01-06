def solution(board):
    answer = 0
    dic = {}
    def checkLen(y,x):
        if 0 <= y <= len(board)-1:
            if 0 <= x <= len(board)-1:
                return True
        return False
    def godic(y,x):
        dic[(y,x)] = 1
        
        if checkLen(y-1,x-1):
            dic[(y-1,x-1)] = 1
        if checkLen(y-1,x):
            dic[(y-1,x)] = 1
        if checkLen(y-1,x+1):
            dic[(y-1,x+1)] = 1
            
        if checkLen(y,x-1):
            dic[(y,x-1)] = 1
        if checkLen(y,x+1):
            dic[(y,x+1)] = 1
            
        if checkLen(y+1,x-1):
            dic[(y+1,x-1)] = 1
        if checkLen(y+1,x):
            dic[(y+1,x)] = 1
        if checkLen(y+1,x+1):
            dic[(y+1,x+1)] = 1
        
    arr = [[0]* len(board) for _ in range(len(board))]
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x] == 1:
                godic(y,x)

    return len(board)*len(board)-len(dic)