def solution(board, k):
    answer = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if y + x <= k:
                answer += board[y][x]
    return answer