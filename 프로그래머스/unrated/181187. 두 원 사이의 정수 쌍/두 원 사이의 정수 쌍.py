import math

def solution(r1, r2):
    answer = 0
    
    r1r1 = r1*r1
    r2r2 = r2*r2
    
    r2answer = 0
    
    for y in range(0,r2):
        temp = math.sqrt(r2r2 - y*y)
        
        r2answer += math.floor(temp)
    
    # print(r2answer*4 + 1)
    

    r1answer = 0
    for y in range(0,r1):
        temp = math.sqrt(r1r1 - y*y)
        temp2 = math.floor(temp)
        
        if temp == temp2:
            r1answer -= 1
            
        r1answer += temp2
            
    # print(r1answer*4+1)

    return (r2answer-r1answer)*4