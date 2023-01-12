def solution(s):
    answer = []  
    
    s = sorted(eval(s[1:-1]))
    
    if len(s) == 1:
        return s
    else:
        for i in s[0]:
            answer.append(i)

    for i in range(1,len(s)):
        for i in s[i]-s[i-1]:
            answer.append(i)
    
    return answer