def solution(topping):
    answer = 0
    dicB = {}
    dicA = {}
    lB = 0
    lA = 0
    
    for i in topping:
        if dicB.get(i):
            dicB[i] += 1
        else:
            dicB[i] = 1
            
    lB = len(dicB)
    for i in topping:
        if not dicA.get(i):
            dicA[i] = 1
        
        dicB[i] -= 1
        if dicB[i] == 0:
            lB -= 1
        
        lA = len(dicA)
        
        if lA == lB:
            answer += 1
        
    return answer