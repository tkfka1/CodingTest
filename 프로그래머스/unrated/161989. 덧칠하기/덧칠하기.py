from collections import deque

def solution(n, m, section):
    answer = 0
    
    ds = deque(section)
    
    while True:
        if ds:
            answer += 1
            temp = ds.popleft()
            temp2 = temp + m-1
            while True:
                if ds:
                    if ds[0] <= temp2:
                        ds.popleft()
                    else:
                        break
                else:
                    break     
        else:
            break
    
    return answer