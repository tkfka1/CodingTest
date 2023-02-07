def solution(s, skip, index):
    answer = ''
    
    alpa = [chr(i) for i in range(97,123)]
    
    for i in skip:
        alpa.remove(i)
    
    print(len(alpa))
    
    for i in s:
        x = alpa.index(i)+index
        while True:
            if x >= len(alpa):
                x -= len(alpa)
            else:
                break
        answer += alpa[x]
    

    
    
    
    return answer