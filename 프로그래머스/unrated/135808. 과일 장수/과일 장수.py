def solution(k, m, score):
    answer = 0

    score = sorted(score,reverse = True)
    count = 0
    for i in score:
        count += 1
        if count == m:
            count = 0
            answer += i*m
    
    return answer