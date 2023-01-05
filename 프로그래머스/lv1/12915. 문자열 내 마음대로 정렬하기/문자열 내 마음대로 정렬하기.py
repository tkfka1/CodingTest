def solution(strings, n):
    answer = []
    
    if n == 0:
        return sorted(strings)
    
    for i in strings:
        i = i[n]+i[:n]+i[n+1:]
        answer.append(i)
        
#     print(answer)
    answer = sorted(answer)
    # print(answer)
    
    for i in range(len(answer)):
        answer[i] = answer[i][1:n+1] + answer[i][0]  + answer[i][n+1:]
    # print(answer)
        
    return answer