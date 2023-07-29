def solution(intStrs, k, s, l):
    answer = []
    
    for i in intStrs:
        temp = int(i[s:s+l])
        if k < int(temp):
            answer.append(temp)
    
    
    return answer