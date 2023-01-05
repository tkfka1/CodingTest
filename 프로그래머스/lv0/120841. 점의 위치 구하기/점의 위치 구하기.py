def solution(dot):
    answer = 1
    if dot[0] < 0:
        answer += 1
    if dot[1] < 0:
        answer += 1
        if dot[0] > 0:
            answer += 2
    
    return answer