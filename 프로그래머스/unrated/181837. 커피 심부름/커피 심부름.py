def solution(order):
    answer = 0
    for i in order:
        if i[0] == "a" or i[3] == "r" or i[3] == "a":
            answer += 4500
        else:
            answer += 5000
    return answer