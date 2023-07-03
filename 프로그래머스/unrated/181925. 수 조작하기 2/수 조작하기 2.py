def solution(numLog):
    answer = ''
    for k,v in enumerate(numLog):
        if k != 0:
            x = numLog[k] - numLog[k - 1]
            if x == 1:
                answer+="w"
            elif x == -1:
                answer += "s"
            elif x == 10:
                answer += "d"
            else:
                answer += "a"
        
    return answer