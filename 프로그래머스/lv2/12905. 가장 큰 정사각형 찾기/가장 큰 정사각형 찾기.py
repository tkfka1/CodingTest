def solution(board):
    answer = 0
    no_zero = 0
    y_len = len(board)
    x_len = len(board[0])
    
    
    for y in range(1, y_len):
        for x in range(1, x_len):
            if board[y][x] == 1:
                board[y][x] = min(board[y-1][x],board[y][x-1],board[y-1][x-1]) +1

    return max([max([x for x in board[y]]) for y in range(y_len)])**2