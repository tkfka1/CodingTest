def solution(n):
    answer = []
    for y in range(n):
        temp = []
        for x in range(n):
            if y == x:
                temp.append(1)
            else:
                temp.append(0)
        answer.append(temp)
    return answer