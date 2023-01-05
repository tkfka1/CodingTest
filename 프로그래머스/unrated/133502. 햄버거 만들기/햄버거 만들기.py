from collections import deque

def solution(ingredient):
    answer = 0
    dq1=deque(ingredient[1:])
    dq2=deque([ingredient[0]])
    ansli = deque([1,2,3,1])
    

    
    while True:
        stack = answer
        for i in range(len(dq1)):
            dq2.append(dq1.popleft())
            if len(dq2) > 3:
                if dq2[-1] == 1:
                    if dq2[-2] == 3:
                        if dq2[-3] == 2:
                            if dq2[-4] == 1:
                                dq2.pop()
                                dq2.pop()
                                dq2.pop()
                                dq2.pop()
                                answer+=1
        if stack == answer:
            break
    

    return answer