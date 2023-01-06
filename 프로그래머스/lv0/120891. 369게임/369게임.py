def solution(order):
    answer = 0
    li369 = ["3","6","9"]
    for i in str(order):
        if i in li369:
            answer += 1
    return answer