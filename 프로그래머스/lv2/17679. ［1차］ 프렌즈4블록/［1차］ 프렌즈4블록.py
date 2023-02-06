def solution(m, n, board):
    answer = 0
    
    def go(board,answer):
        answer_temp = answer
        li = [[0]*n for _ in range(m)]
        li2 = []
        for y in range(m-1):
            for x in range(n-1):
                temp = board[y][x]
                if not temp == "0":
                    if board[y+1][x] == temp:
                        if board[y][x+1] == temp:
                            if board[y+1][x+1] == temp:
                                li[y][x] = 1
                                li[y+1][x] = 1
                                li[y][x+1] = 1
                                li[y+1][x+1] = 1
        for x in range(n):
            temp = ""
            for y in reversed(range(m)):
                if li[y][x] == 0:
                    temp += board[y][x]
                else:
                    answer_temp += 1

            temp+="0"*(m-len(temp))
            li2.append(temp)

        temp = ["" for _ in range(m)]
        for y in range(len(li2)):
            for x in range(len(li2[y])):
                temp[m-x-1] += li2[y][x]
        
        if answer_temp == answer:
            return answer
        return go(temp,answer_temp)

    return go(board,answer)