from collections import deque
def solution(A, B):
    answer = 0
    if A == B:
        return 0
    
    A = deque(A)
    B = deque(B)

    for i in range(len(A)-1):
        temp = A.pop()
        A.appendleft(temp)
        answer += 1
        if A == B:
            return answer
        
    return -1