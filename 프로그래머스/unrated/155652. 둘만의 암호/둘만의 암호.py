def solution(s, skip, index):
    answer = ''
    
    alpa = [chr(i) for i in range(97,123)]
    
    for i in skip:
        alpa.remove(i)
    
    for i in s:
        x = alpa.index(i)+index
        x = x%len(alpa)
        answer += alpa[x]
    
    return answer