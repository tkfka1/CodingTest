def solution(myString):
    answer = ''
    for i in myString:
        if ord(i) < 108:
            answer += "l"
        else:
            answer += i
    return answer