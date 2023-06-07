def solution(strArr):
    answer = []
    for k,v in enumerate(strArr):
        if k %2 == 0:
            answer.append(v.lower())
        else:
            answer.append(v.upper())
    return answer