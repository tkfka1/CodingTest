def solution(board, skill):
    answer = 0

    def nu(list,cal):
        d = cal[5]
        if cal[0] == 1:
            d = -cal[5]
        list[cal[1]][cal[2]] += d
        list[cal[3]+1][cal[4]+1] += d
        list[cal[1]][cal[4]+1] -= d
        list[cal[3]+1][cal[2]] -= d
        return list
    def nusum(list):
        for y in range(len(list)):
            for x in range(len(list[0])):
                if not list[y][x] == 0 or not x == len(list[0])-1:
                    list[y][x+1] += list[y][x]
        for y in range(len(list)):
            for x in range(len(list[0])):
                if not list[y][x] == 0 or not y == len(list)-1:
                    list[y+1][x] += list[y][x]

        return list

    list = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for i in skill:
        nu(list,i)
    nusum(list)
    for y in range(len(board)):
        for x in range(len(board[0])):
            board[y][x] += list[y][x]
            if board[y][x] > 0:
                answer += 1

    return answer