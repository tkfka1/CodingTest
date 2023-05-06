from collections import deque
def solution(targets):
    answer = 0
    
    tli = deque([])
    for i in sorted(targets):
        tli.append(i)
    
    while True:
        temp = tli.popleft()
        
        while True:     
            if not tli:
                break
            if temp[1] > tli[0][0]:
                temp2 = tli.popleft()
                if temp2[1] < temp[1]:
                    temp = temp2
            else:
                break
        
        answer += 1
        
        if not tli:
            break
    
    return answer